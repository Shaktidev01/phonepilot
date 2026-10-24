# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""The stdio ADB server hands screenshots to the client as real MCP images."""

import base64
import io

from mcp.types import ImageContent, TextContent
from PIL import Image
import pytest

from phonepilot.mcp import adb_server


def _jpeg_b64() -> str:
    buf = io.BytesIO()
    Image.new("RGB", (4, 4), "red").save(buf, "JPEG")
    return base64.b64encode(buf.getvalue()).decode()


class _FakeController:
    def __init__(self, screenshot_b64: str | None = None, error: Exception | None = None):
        self._b64 = screenshot_b64
        self._error = error

    async def take_screenshot(self) -> str:
        if self._error:
            raise self._error
        assert self._b64 is not None
        return self._b64


def _blocks(result):
    # FastMCP returns either the content list or (content, structured) depending on version.
    return result[0] if isinstance(result, tuple) else result


@pytest.mark.asyncio
async def test_take_screenshot_returns_an_image_block(monkeypatch):
    data = _jpeg_b64()
    monkeypatch.setattr(adb_server, "_get_controller", lambda *a, **k: _FakeController(data))

    blocks = _blocks(await adb_server.mcp.call_tool("take_screenshot", {}))

    assert len(blocks) == 1
    assert isinstance(blocks[0], ImageContent)
    assert blocks[0].mimeType == "image/jpeg"
    assert blocks[0].data == data


@pytest.mark.asyncio
async def test_take_screenshot_reports_device_errors_as_text(monkeypatch):
    monkeypatch.setattr(
        adb_server, "_get_controller", lambda *a, **k: _FakeController(error=RuntimeError("boom"))
    )

    blocks = _blocks(await adb_server.mcp.call_tool("take_screenshot", {}))

    assert len(blocks) == 1
    assert isinstance(blocks[0], TextContent)
    assert blocks[0].text == "Error: boom"

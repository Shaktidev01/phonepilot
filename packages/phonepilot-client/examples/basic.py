"""Run one task against an PhonePilot host."""

import asyncio
import os

from phonepilot_client import PhonePilotClient


async def main() -> None:
    client = PhonePilotClient(
        os.environ.get("PHONEPILOT_BASE_URL", "http://127.0.0.1:8000"),
        token=os.environ.get("PHONEPILOT_TOKEN"),
    )

    devices = await client.list_devices()
    if not devices:
        raise RuntimeError("The PhonePilot host did not report an Android device")

    result = await client.run(
        "Open the Battery page in Android Settings and verify the battery percentage.",
        profile="flash",
        device_serial=devices[0].serial,
    )
    if not result.succeeded:
        raise RuntimeError(result.error or f"Task ended with status {result.status}")
    print(f"Task {result.task_id} completed on {result.device_serial}")


if __name__ == "__main__":
    asyncio.run(main())

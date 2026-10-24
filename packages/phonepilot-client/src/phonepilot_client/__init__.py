# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0

"""Public API for the lightweight PhonePilot remote client."""

from phonepilot_client.client import PhonePilotClient
from phonepilot_client.errors import (
    ApiError,
    PhonePilotClientError,
    AuthenticationError,
    ConflictError,
    NetworkError,
    NotFoundError,
    ProtocolError,
    TaskRejectedError,
    TaskTimeoutError,
)
from phonepilot_client.models import Capabilities, Device, TaskHandle, TaskResult
from phonepilot_client.transport import JsonTransport

__version__ = "0.1.0"

__all__ = [
    "ApiError",
    "PhonePilotClient",
    "PhonePilotClientError",
    "AuthenticationError",
    "Capabilities",
    "ConflictError",
    "Device",
    "JsonTransport",
    "NetworkError",
    "NotFoundError",
    "ProtocolError",
    "TaskHandle",
    "TaskRejectedError",
    "TaskResult",
    "TaskTimeoutError",
    "__version__",
]

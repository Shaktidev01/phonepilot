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

"""PhonePilot cross-platform runtime and process supervisor subsystem."""

from phonepilot.runtime.device_lock import (
    ConcurrencyMode,
    DeviceBusyError,
    DeviceExecutionLock,
)
from phonepilot.runtime.adb_endpoint import (
    ADB_ENDPOINT_ID_ENV,
    AdbEndpoint,
    AdbSession,
    AdbTarget,
    InvalidAdbEndpoint,
    current_adb_endpoint,
)
from phonepilot.runtime.device_pool import DevicePool, DeviceStatus, device_pool
from phonepilot.runtime.process_probe import pid_is_alive
from phonepilot.runtime.daemon_client import (
    ensure_daemon_running,
    get_daemon_session,
    get_daemon_status,
    is_phonepilot_daemon,
    is_daemon_running,
    stop_task_on_daemon,
    submit_batch_to_daemon,
    submit_task_to_daemon,
    wait_for_daemon_task,
)
from phonepilot.runtime.awake_service import (
    ensure_device_awake,
    sanitize_device_state,
    screen_awake_service,
    shutdown_awake_service,
    start_awake_service,
)
from phonepilot.runtime.server_lifecycle import (
    clear_server_info,
    find_server_pids,
    get_server_status,
    is_port_in_use,
    read_server_info,
    stop_server,
    write_server_info,
)
from phonepilot.runtime.supervisor import ProcessSupervisor, process_supervisor
from phonepilot.runtime.cancel_requests import (
    clear_cancel_request,
    is_cancel_requested,
    request_cancel,
    watch_for_cancel_request,
)

__all__ = [
    "ADB_ENDPOINT_ID_ENV",
    "AdbEndpoint",
    "AdbSession",
    "AdbTarget",
    "ConcurrencyMode",
    "DeviceBusyError",
    "DeviceExecutionLock",
    "DevicePool",
    "DeviceStatus",
    "InvalidAdbEndpoint",
    "clear_cancel_request",
    "clear_server_info",
    "current_adb_endpoint",
    "device_pool",
    "ensure_daemon_running",
    "ensure_device_awake",
    "find_server_pids",
    "get_daemon_session",
    "get_daemon_status",
    "get_server_status",
    "is_phonepilot_daemon",
    "is_daemon_running",
    "is_cancel_requested",
    "is_port_in_use",
    "pid_is_alive",
    "ProcessSupervisor",
    "process_supervisor",
    "read_server_info",
    "request_cancel",
    "sanitize_device_state",
    "screen_awake_service",
    "shutdown_awake_service",
    "start_awake_service",
    "stop_server",
    "stop_task_on_daemon",
    "submit_batch_to_daemon",
    "submit_task_to_daemon",
    "wait_for_daemon_task",
    "watch_for_cancel_request",
    "write_server_info",
]

# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0

"""Compatibility import for the standalone remote PhonePilot client.

The implementation lives in the zero-dependency ``phonepilot-client`` package.
Keeping this module lets existing full-runtime installations migrate without
maintaining a second client execution path.
"""

from phonepilot.runtime import ConcurrencyMode
from phonepilot_client import PhonePilotClient

__all__ = ["PhonePilotClient", "ConcurrencyMode"]

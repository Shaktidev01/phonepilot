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

"""Parts of mobile-use (Minitap, Inc.) used by PhonePilot. See LICENSE and METADATA."""

# phonepilot and these modules import each other. Import phonepilot first so that
# importing one of these modules directly works the same as going through phonepilot.
import phonepilot  # noqa: F401, E402

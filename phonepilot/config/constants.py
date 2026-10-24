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

"""Centralized constants, environment variable names, and type definitions for PhonePilot."""

from typing import Literal

# ==============================================================================
# Environment Variable Keys
# ==============================================================================

# Application & Workspace Paths
ENV_PHONEPILOT_APP_DIR = "PHONEPILOT_APP_DIR"
ENV_ANTIGRAVITY_APP_DIR = "ANTIGRAVITY_APP_DIR"
ENV_PHONEPILOT_USE_USER_DIR = "PHONEPILOT_USE_USER_DIR"
ENV_PHONEPILOT_TRACES_DIR = "PHONEPILOT_TRACES_DIR"
ENV_DATA_ENGINE_DB_PATH = "DATA_ENGINE_DB_PATH"

# Cloud Brain & Distributed Execution
ENV_PHONEPILOT_CLOUD_MODE = "PHONEPILOT_CLOUD_MODE"
ENV_PHONEPILOT_CLOUD_SESSION_ID = "PHONEPILOT_CLOUD_SESSION_ID"
ENV_PHONEPILOT_CLOUD_GATEWAY_URL = "PHONEPILOT_CLOUD_GATEWAY_URL"
ENV_PHONEPILOT_TENANT_ID = "PHONEPILOT_TENANT_ID"
ENV_PHONEPILOT_TENANT_TOKEN = "PHONEPILOT_TENANT_TOKEN"
ENV_PHONEPILOT_EDGE_PORT = "PHONEPILOT_EDGE_PORT"

# Runtime State & IPC
ENV_PHONEPILOT_IPC_PORT = "PHONEPILOT_IPC_PORT"
ENV_ANTIGRAVITY_LS_ADDRESS = "ANTIGRAVITY_LS_ADDRESS"
ENV_PHONEPILOT_MCP_SERVER = "PHONEPILOT_MCP_SERVER"

# Device & ADB
ENV_ADB_DEVICE_SERIAL = "ADB_DEVICE_SERIAL"
ENV_PHONEPILOT_DEVICE_ID = "PHONEPILOT_DEVICE_ID"
ENV_ADB_HOST = "ADB_HOST"
ENV_ADB_PORT = "ADB_PORT"
ENV_ADB_SERVER_SOCKET = "ADB_SERVER_SOCKET"
# UI hierarchy backend: "auto" (helper, UIAutomator2 fallback), "helper", "uiautomator"
ENV_PHONEPILOT_HIERARCHY_BACKEND = "PHONEPILOT_HIERARCHY_BACKEND"
# "true" (default) lets a task install / upgrade the Accessibility Helper APK on a
# device it holds; "false" only attaches to a helper someone installed by hand.
ENV_PHONEPILOT_HELPER_AUTO_INSTALL = "PHONEPILOT_HELPER_AUTO_INSTALL"

# LLM & Vision OCR API Keys
ENV_GOOGLE_API_KEY = "GOOGLE_API_KEY"
ENV_GEMINI_API_KEY = "GEMINI_API_KEY"
ENV_GCP_API_KEY = "GCP_API_KEY"
ENV_OCR_API_KEY = "OCR_API_KEY"
ENV_VISION_API_KEY = "VISION_API_KEY"
ENV_API_KEY = "API_KEY"
ENV_OPENAI_API_KEY = "OPENAI_API_KEY"
ENV_OPENAI_BASE_URL = "OPENAI_BASE_URL"
ENV_ANTHROPIC_API_KEY = "ANTHROPIC_API_KEY"
ENV_OPEN_ROUTER_API_KEY = "OPEN_ROUTER_API_KEY"
ENV_XAI_API_KEY = "XAI_API_KEY"

# Explorer & Agent Defaults
ENV_PHONEPILOT_EXPLORER_VERSION = "PHONEPILOT_EXPLORER_VERSION"
ENV_PHONEPILOT_DEFAULT_PROFILE = "PHONEPILOT_DEFAULT_PROFILE"
ENV_PHONEPILOT_DEFAULT_MODEL = "PHONEPILOT_DEFAULT_MODEL"
ENV_PHONEPILOT_USE_FILE_API = "PHONEPILOT_USE_FILE_API"

# Debugging & Output Paths
ENV_KEEP_VIDEOS = "KEEP_VIDEOS"
ENV_PHONEPILOT_DEBUG = "PHONEPILOT_DEBUG"
ENV_EVENTS_OUTPUT_PATH = "EVENTS_OUTPUT_PATH"
ENV_RESULTS_OUTPUT_PATH = "RESULTS_OUTPUT_PATH"


# ==============================================================================
# Configuration Filenames
# ==============================================================================

PHONEPILOT_CONFIG_FILENAME = "phonepilot.jsonc"
LLM_CONFIG_FILENAME = "llm-config.json"
LLM_CONFIG_OVERRIDE_FILENAME = "llm-config.override.jsonc"
AGENT_CONFIG_FILENAME = "agent_config.json"
DATA_ENGINE_DB_FILENAME = "data_engine.db"
IPC_PORT_FILENAME = ".phonepilot_ipc_port"
LS_ADDRESS_FILENAME = ".jetski_ls_address"
SERVER_INFO_FILENAME = ".phonepilot_server.json"
PAUSE_FILENAME = ".phonepilot_paused"
REPLAY_DIRNAME = "replay"
TEST_DATA_DIRNAME = "data"
TEST_OUTPUTS_DIRNAME = "outputs"
IMAGES_DIRNAME = "images"
DOTENV_FILENAME = ".env"


# ==============================================================================
# Default Values & Network Ports
# ==============================================================================

DEFAULT_ADB_HOST = "127.0.0.1"
DEFAULT_ADB_PORT = 5037
DEFAULT_GATEWAY_PORT = 8000
DEFAULT_EDGE_MONITOR_PORT = 8000
DEFAULT_ACTION_TIMEOUT = 30.0
DEFAULT_STREAM_PING_INTERVAL = 15.0

DEFAULT_PROFILE = "pro"
DEFAULT_MODEL = "gemini-2.5-flash"
DEFAULT_EXPLORER_VERSION: Literal["flash", "pro", "ultra"] = "flash"


# ==============================================================================
# Literals and Type Aliases
# ==============================================================================

LLMProvider = Literal[
    "openai", "google", "openrouter", "xai", "vertexai", "anthropic", "ollama", "vllm", "custom"
]
ExplorerVersion = Literal["flash", "pro", "ultra"]

LLMUtilsNode = Literal[
    "outputter",
    "hopper",
    "video_analyzer",
    "object_detector",
]

AgentNode = Literal[
    "planner",
    "summarizer",
    "operator",
    "operator_summarizer",
    "log_reader_sub_agent",
    "log_analyzer",
    "diagnoser",
    "checker",
    "planner_avatar",
    "history_analyzer_expert",
    "diagnoser_expert",
    "explorer",
    "history_analyzer",
    "validator_pixel_safety_net",
    "planner_validation",
    "validator",
    "output_analyzer",
]

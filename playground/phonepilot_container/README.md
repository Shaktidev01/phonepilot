# 🤖 PhonePilot Session Container

Dedicated, session-isolated container image for running the PhonePilot Autonomous AI Agent on Google Cloud **Container-Optimized OS (COS)**.

---

## 📌 Architecture & Lifecycle

When a user initiates a session via the [Backend Manager](file:///usr/local/google/home/yaoyaogoogle/develop/phonepilot/playground/backend_manager/README.md), the backend dynamically spawns an instance of this container named `phonepilot-session-<session_id>` on the shared `phonepilot-net` bridge network.

```mermaid
flowchart LR
    subgraph COS_Host["COS VM Host Network"]
        CVD["Cuttlefish AVD Emulator\n(Port: 6520+N)"]
    end

    subgraph PhonePilotContainer["PhonePilot Session Container (phonepilot-session-:id)"]
        Entrypoint["docker-entrypoint.sh\n(adb connect host.docker.internal:6520)"]
        Server["PhonePilot Server (:8080)\n- apps.admin_console.server\n- Agent Task Loop\n- SSE Stream (/stream/events)"]
    end

    subgraph NginxProxy["Nginx Reverse Proxy"]
        Ingress["/session/:id/phonepilot/*"]
    end

    Entrypoint -->|ADB TCP Link| CVD
    Server -->|Screen Capture & Dynamic Touch Events| CVD
    Ingress -->|Dynamic Proxy (127.0.0.11)| Server
```

---

## 🔑 Key Features

1. **Automated ADB Bridging**:
   - The container entrypoint ([docker-entrypoint.sh](file:///usr/local/google/home/yaoyaogoogle/develop/phonepilot/playground/phonepilot_container/docker-entrypoint.sh)) automatically connects to the target Cuttlefish instance using `$ADB_DEVICE_SERIAL` (e.g. `host.docker.internal:6520`) with automatic retry handling.

2. **Multimodal Perception & Toolchain**:
   - Packaged with Android Platform Tools (`adb`), `ffmpeg`, OpenCV libraries (`libgl1`, `libglib2.0-0`), and Python 3.12.

3. **Real-time Event Streaming**:
   - Hosts the PhonePilot Admin Console server exposing SSE and WebSocket endpoints (`/stream/events`) for live streaming agent reasoning, thought steps, and action execution directly to the frontend.

4. **Dynamic Selector & Coordinate Fallback Engine**:
   - Drives real-time automated navigation on the connected Cuttlefish emulator using PhonePilot's multimodal reasoning pipeline.

---

## 📁 Directory Structure

```
playground/phonepilot_container/
├── Dockerfile                   # Python 3.12 slim with adb, ffmpeg, OpenCV, and PhonePilot
├── docker-entrypoint.sh         # Automated ADB connection loop & service startup
├── docker-compose.yml           # Compose spec for testing standalone session
├── .dockerignore
└── README.md                    # Documentation & operational guide
```

---

## ⚙️ Environment Variables

| Variable | Default | Description |
| :--- | :--- | :--- |
| `SESSION_ID` | `standalone-dev` | Unique session UUID passed by the Backend Manager |
| `ADB_DEVICE_SERIAL` | `host.docker.internal:6520` | TCP host and port of the target Cuttlefish emulator |
| `PORT` | `8080` | Port for PhonePilot Admin & Stream server |
| `PYTHONUNBUFFERED` | `1` | Ensures immediate stdout logging |
| `GEMINI_API_KEY` | - | Google Gemini API key for agent reasoning |
| `OPENAI_API_KEY` | - | Optional OpenAI API key |

---

## 🚀 Building & Running

### 1. Build the PhonePilot Container Image
From the repository root:
```bash
docker build -f playground/phonepilot_container/Dockerfile -t phonepilot:latest .
```

### 2. Run Standalone with Docker CLI
```bash
# Ensure bridge network exists
docker network create phonepilot-net || true

# Run PhonePilot session container targeting Cuttlefish on port 6520
docker run -d \
  --name phonepilot-session-sample \
  --network phonepilot-net \
  --add-host host.docker.internal:host-gateway \
  -e SESSION_ID=sample-123 \
  -e ADB_DEVICE_SERIAL=host.docker.internal:6520 \
  -e GEMINI_API_KEY="your-gemini-key" \
  -p 8080:8080 \
  phonepilot:latest
```

### 3. Run with Docker Compose (Test Setup)
```bash
cd playground/phonepilot_container
docker-compose up -d
```

---

## 🧪 Verification & Health Check

1. **Verify ADB Connection inside Container**:
   ```bash
   docker exec -it phonepilot-session-sample adb devices
   ```

2. **Verify Server Health Probe**:
   ```bash
   curl http://localhost:8080/api/system/health
   # Returns: {"status": "ok", ...}
   ```

3. **Verify Trace Streaming**:
   ```bash
   curl -N http://localhost:8080/stream/events
   # Real-time Server-Sent Events stream
   ```

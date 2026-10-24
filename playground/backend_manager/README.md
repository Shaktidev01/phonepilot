# 🚀 PhonePilot Backend Manager Container

The central orchestration, API gateway, authentication, and container lifecycle service for running PhonePilot and Cuttlefish on Google Cloud **Container-Optimized OS (COS)**.

---

## 📌 Core Responsibilities

1. **Authentication & OTP Callbacks**:
   - Manages user verification (`POST /api/v1/auth/otp/send` and `POST /api/v1/auth/otp/verify`).
   - Issues signed JWT access tokens for secure tenant separation.
   - Provides session validation hooks for Nginx ingress (`/api/v1/auth/validate-session`).

2. **Docker Socket Container Orchestration**:
   - Communicates with `/var/run/docker.sock` to dynamically spawn `phonepilot-session-<session_id>` containers on the shared `phonepilot-net` bridge network.
   - Injects runtime environment variables (`SESSION_ID`, `ADB_DEVICE_SERIAL`, `PORT=8080`).
   - Automatically executes `adb connect` inside the container to pair it with the Cuttlefish emulator.

3. **Cloud Orchestrator & Cuttlefish Integration**:
   - Dispatches API requests to the Cloud Orchestrator service running on COS to spin up dedicated Cuttlefish AVDs.
   - Binds allocated ADB ports (`6520+N`) and WebRTC signaling ports (`8443+N`).

4. **BigQuery Mapping Store**:
   - Tracks metadata linking `user_id`, `session_id`, `phonepilot_container_id`, `cuttlefish_adb_port`, `cuttlefish_webrtc_port`, and timestamps.
   - Includes automatic partitioned table creation on BigQuery (`phonepilot_orchestration.sessions_registry`) and an in-memory fallback for local dev.

5. **Static Frontend UI Host**:
   - Serves the dual-pane web application (Cuttlefish WebRTC stream player + PhonePilot agent thought workspace) at `/`.

6. **Automatic Session Reaper & Watchdog**:
   - Background periodic worker checks active sessions every 30s.
   - Automatically destroys orphaned containers and AVDs when the session TTL expires or heartbeat fails.

---

## 📁 Directory Structure

```
playground/backend_manager/
├── Dockerfile                   # Python 3.12 slim image with health check
├── docker-compose.yml           # Compose spec with /var/run/docker.sock mount
├── requirements.txt             # FastAPI, Pydantic, Docker SDK, BigQuery, JWT
├── README.md                    # Detailed documentation
└── app/
    ├── main.py                  # FastAPI app entrypoint with lifespan manager
    ├── config.py                # Environment configuration settings
    ├── auth/
    │   ├── jwt_handler.py       # JWT encoding/decoding & get_current_user dependency
    │   └── otp_service.py       # OTP generation, storage, and verification
    ├── services/
    │   ├── docker_service.py    # Docker socket manager (start/stop containers)
    │   ├── cloud_orchestrator_service.py # Cloud Orchestrator Cuttlefish client
    │   ├── bigquery_service.py  # BigQuery mapping repository with local fallback
    │   └── session_manager.py   # Master session lifecycle & reaper coordinator
    ├── routers/
    │   ├── auth_router.py       # OTP and JWT endpoints
    │   ├── session_router.py    # Session creation, polling, heartbeat, and deletion
    │   └── health_router.py     # Liveness probe endpoint (/healthz)
    ├── schemas/
    │   ├── auth_schema.py       # Auth request/response schemas
    │   └── session_schema.py    # Session & mapping schemas
    └── static/
        ├── index.html           # Dual-pane glassmorphic web workspace
        ├── style.css            # Aurora design system styling
        └── app.js               # Frontend client logic & streaming hooks
```

---

## 🔌 REST API Endpoints

### Authentication
* `POST /api/v1/auth/otp/send` — Request a 6-digit OTP code (`{"identifier": "user@example.com"}`).
* `POST /api/v1/auth/otp/verify` — Verify OTP code and receive signed JWT token (`{"identifier": "...", "code": "123456"}`).
* `GET /api/v1/auth/me` — Return profile of the current authenticated user (`Authorization: Bearer <jwt>`).
* `GET /api/v1/auth/validate-session?session_id=...` — Validate user authorization for a specific session.

### Sessions & Container Management
* `POST /api/v1/sessions/create` — Provision Cuttlefish AVD + PhonePilot container, link ADB, and register mapping.
* `GET /api/v1/sessions` — List all active sessions for the current user.
* `GET /api/v1/sessions/{session_id}` — Get session status and reverse-proxy stream endpoints.
* `POST /api/v1/sessions/{session_id}/heartbeat` — Send client heartbeat to extend session TTL.
* `DELETE /api/v1/sessions/{session_id}` — Terminate container and release Cuttlefish instance.

### Health Probe
* `GET /healthz` — Returns `200 OK` with service health status.

---

## ⚙️ Environment Variables

| Variable | Default | Description |
| :--- | :--- | :--- |
| `PORT` | `8000` | HTTP port to listen on |
| `APP_ENV` | `development` | Environment mode (`development` / `production`) |
| `JWT_SECRET_KEY` | `phonepilot-...` | Secret key for signing JWT session tokens |
| `DOCKER_SOCKET_PATH` | `unix://var/run/docker.sock` | Path to host Docker daemon socket |
| `DOCKER_NETWORK` | `phonepilot-net` | Shared bridge network for dynamic container routing |
| `PHONEPILOT_IMAGE` | `phonepilot:latest` | Docker image to spawn for PhonePilot instances |
| `CLOUD_ORCHESTRATOR_URL` | `http://host.docker.internal:1443` | Endpoint of the Cloud Orchestrator service |
| `CUTTLEFISH_HOST_GATEWAY` | `host.docker.internal` | Host IP / gateway for ADB TCP connections |
| `GOOGLE_CLOUD_PROJECT` | `phonepilot-cloud-project` | GCP project ID for BigQuery dataset |
| `USE_LOCAL_FALLBACK_DB` | `true` | Enables in-memory DB fallback if BigQuery is unconfigured |
| `SESSION_TTL_MINUTES` | `60` | Default session lifespan before automatic teardown |

---

## 🚀 Running the Container

### 1. Build Image
```bash
docker build -t phonepilot-backend-manager:latest .
```

### 2. Run with Docker Compose
```bash
docker-compose up -d
```

### 3. Run Standalone with Docker on COS
```bash
docker run -d \
  --name backend \
  --restart unless-stopped \
  --network phonepilot-net \
  --add-host host.docker.internal:host-gateway \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -p 8000:8000 \
  phonepilot-backend-manager:latest
```

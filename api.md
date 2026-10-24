# SuperSeedance API notes

The hosted application's [API reference](https://superseedance.si/api-reference.md) documents server-to-server API keys as well as browser sessions. [Human-readable API docs](https://superseedance.si/en/docs) explain the workflow.

## MCP access

The [MCP guide](mcp.md) covers `https://superseedance.si/api/mcp`, account API-key authentication, read-only tools and paid video creation. Use a compatible server-side client; this endpoint does not provide OAuth. Quote the selected settings and obtain explicit approval before creating a paid task.

MCP protocol and tool behavior have been tested locally. This does not establish compatibility with every client; verify a connection with read-only tools before enabling paid creation.

## Authentication

Create a key in a verified account's settings. Server requests use `Authorization: Bearer YOUR_STUDIO_API_KEY` and must not send browser `Origin`, `Cookie` or `Sec-Fetch-Site` headers. Store the key on your backend. Account and key management still use the signed-in browser session; API keys do not bypass email verification, resource ownership or available credits.

## Existing endpoints

| Endpoint | Purpose |
|---|---|
| `GET /api/studio/config` | Public generation, analysis and payment availability |
| `POST /api/quote` | Public credit calculation without creating a task |
| `POST /api/generate` | Create a generation task using a unique idempotency key |
| `GET /api/jobs` | List the authenticated owner's jobs |
| `GET /api/jobs/{id}` | Read an owned task's status |
| `GET /api/jobs/{id}/video` | Retrieve an owned completed video's bytes |
| `GET /api/billing` | Read the owner's credit balance and billing records |

Do not interpret a configured API as proof of live payment acceptance. At the October 24, 2026 read-only check, generation and email were configured, while purchases and AI video-frame analysis were unavailable. We did not perform a paid server-key generation in this documentation check.

Use the live reference for request fields, limits, error states and availability. This repository does not provide an SDK or promise an OpenAI-compatible API.

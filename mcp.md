# SuperSeedance MCP

Use a compatible server-side MCP client to check Seedance settings, quote video credits and manage your own generation tasks.

| Connection field | Value |
|---|---|
| Endpoint | `https://superseedance.si/api/mcp` |
| Transport | Stateless HTTP POST |
| Authentication | `Authorization: Bearer YOUR_STUDIO_API_KEY` |
| API key | Create in a verified SuperSeedance account's settings |
| Request content type | `application/json` |
| Accepted response types | `application/json, text/event-stream` |

Keep the key in the client's secret storage. Requests must not include browser cookies, `Origin` or `Sec-Fetch-Site`. This connection uses account API keys, not OAuth. A client that only supports browser authorization cannot use this endpoint as configured.

## Tools

- `list_models`: available models, supported settings and worker status.
- `quote_video`: current studio-credit quote for selected settings, without a charge.
- `get_credit_balance`: your credit balance.
- `list_videos`: your saved tasks, with filters and pagination.
- `get_video`: status and private output URL for one of your tasks.
- `create_video`: reserve the approved credits and queue one video.

For paid creation, first obtain a quote, show the user the prompt, settings and cost, and get explicit approval. `create_video` requires `confirmCharge: true`, matching `confirmedCredits` and a unique `idempotencyKey`. A connection or a request for a quote is not permission to spend credits. The queue applies the same balance, availability, ownership and concurrency checks as the website.

Retain the same key and identical request when recovering a network response. Do not automatically start a new paid task. To check progress, call `get_video` about every five seconds and back off on errors. Result URLs require owner authentication.

The endpoint provides no asset upload, URL import, retry, delete, payment or credit-grant tools. To use an image, first upload it through your account or the existing asset API, then pass its owned `assetId`.

## Protocol support

The server supports modern 2026-07-28 requests and legacy stateless initialization, including 2025-11-25. Modern clients must send matching protocol/method/name metadata and headers. No persistent session ID or GET event stream is required. There are no subscriptions.

[Complete API and MCP reference](https://superseedance.si/api-reference.md) · [Generation availability](https://superseedance.si/api/studio/config)

This guide is maintained by SuperSeedance. A working connection or directory entry does not imply endorsement by an AI platform. Production client compatibility should be checked with read-only tools before enabling paid creation.

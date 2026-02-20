PostgreSQL Authentication Failed
❌ Error
FATAL: password authentication failed for user "postgres"

🔍 Root Cause

Local PostgreSQL (postgres.exe) and Docker PostgreSQL were both running

Both were listening on port 5432

Client connections were routed inconsistently

✅ Resolution

Stop local PostgreSQL service:

services.msc → Stop PostgreSQL

Verify only Docker is listening:

netstat -ano | findstr 5432

🧠 Notes

Never run local PostgreSQL and Docker PostgreSQL on the same port.

2️⃣ Docker PostgreSQL 18 Volume Initialization Error
❌ Error
Database is uninitialized and superuser password is not specified

🔍 Root Cause

PostgreSQL 18+ changed internal data directory structure

Volume mounted to /var/lib/postgresql/data caused startup failure

✅ Resolution

Mount volume to:

/var/lib/postgresql


Reset Docker state:

docker compose down -v
docker compose up -d

3️⃣ Environment Variable Changes Not Applied
❌ Symptom

Password or database name changes had no effect

🔍 Root Cause

PostgreSQL environment variables are applied only on first initialization

Existing Docker volumes preserve old credentials

✅ Resolution
docker compose down -v
docker compose up -d

4️⃣ pgcli Crash Due to Timezone Mismatch (Windows)
❌ Error
invalid value for parameter "TimeZone": "Asia/Katmandu"

🔍 Root Cause

Windows timezone (Asia/Katmandu) is not a valid PostgreSQL IANA timezone

Older pgcli versions attempt to set timezone on connect

✅ Resolution (Recommended)

Force UTC before starting pgcli:

export TZ=UTC
uv run pgcli -h localhost -p 5432 -u postgres -d ny_taxi

🔁 Alternative

Use psql instead of pgcli:

docker exec -it ny_taxi_postgres psql -U postgres -d ny_taxi

### SQLAlchemy Connecting to Wrong PostgreSQL Port

**Error**
connection to server at "localhost", port 5432 failed: password authentication failed

pgsql
Copy code

**Cause**
Docker PostgreSQL was exposed on port `5433`, but the SQLAlchemy connection string still pointed to port `5432`, causing connections to hit the local PostgreSQL instance.

**Fix**
Update the SQLAlchemy engine URL to use port `5433`.

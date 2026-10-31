# Smart Mobility Backend

FastAPI modular-monolith backend for the React frontend. The package mirrors the
database domains while keeping HTTP, business, and persistence concerns separate.

## Layout

- `app/api/routes` — REST endpoints and transport concerns.
- `app/schemas` — Pydantic request/response contracts.
- `app/services` — use-case rules and module workflows; services depend on repositories only through `UnitOfWork`.
- `app/repositories` — SQLAlchemy data-access helpers.
- `app/models` — ORM mapping for the supplied SQLite schema.
- `app/core` — configuration, security, utilities, and exceptions.
- `app/database.py` — engine, sessions, and SQLite foreign-key setup.
- `tests` — API and service tests.

## Run

```powershell
python -m pip install -e ".[test]"
python -m uvicorn app.main:app --reload
```

API documentation is available at `http://localhost:8000/docs`.

## Database schema assessment

The supplied `db_schema.sql` is valid SQLite: an in-memory execution created all
23 tables and `PRAGMA foreign_key_check` returned no violations.

SQLAlchemy ORM is appropriate because it provides typed mappings, session/unit-of-work
handling, and one place for migrations and testable repositories. SQLite is suitable
for this course implementation when the database remains single-process and
deployment uses the file-backed SQLite configuration. Enable foreign keys per
connection and prefer PostgreSQL if concurrent writers become a production requirement.

The SQL schema is a usable foundation, but it should be tightened before final use:

- Define lifecycle values as status check constraints and enums in Python.
- Represent timestamps as ISO-8601 `TEXT`, or add migrations that use typed datetime storage.
- Add indexes for reservation, vehicle, hub, status, and telemetry lookup columns.
- Add overlap constraints/application locking for parking, charging, vehicle, and pickup allocation.
- Replace schema-level forward FK references with migration-managed creation order if a migration tool reports issues.
- Add uniqueness/transaction rules for HUB_RESOURCE specialization and only-one-active-policy constraints.

Authentication currently has a placeholder principal. JWT validation, role authorization,
and ownership checks must be implemented before protected endpoints are enabled.

## Application logic implementation

The current backend is intentionally a service skeleton. Domain classes under
`app/services` contain typed workflow contracts, while `app/repositories` contains
data-access responsibilities. Team members should implement business methods in
the service layer and call repositories rather than SQLAlchemy APIs directly.

The intended dependency direction is REST routes -> services -> unit of work ->
repositories -> ORM models. API routes must not construct repositories or call
SQLAlchemy sessions directly. Specialized repositories inherit the small
`BaseRepository` CRUD hierarchy, while domain-specific query methods may be added
to those subclasses without expanding the diagram's base class.

Service methods raise `NotImplementedError` until assigned implementation is
complete. This keeps REST routing, persistence mapping, request schemas, and
application use cases independently maintainable.

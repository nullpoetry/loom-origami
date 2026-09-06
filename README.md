# loom-origami

Development implementation of Loomidi (Origami Nexus) APIs: Loom Data Ingestion, Origami Transformer Control, Learning Loop, and Security Policy Enforcement.

This repository contains API definitions, reference implementations, and CI checks to validate and exercise the OpenAPI contracts for the Loom Data Ingestion and related APIs.

## Quick links

- API specs: docs/api/loom_data_api.yaml

## Overview

The repo provides:

- OpenAPI documents describing the Loom APIs (see docs/api/loom_data_api.yaml).
- Reference code for ingestion and control endpoints (location may vary by language).
- CI workflow that validates OpenAPI specs, lints YAML, runs unit tests, builds Docker images if present, and runs security analysis.

## Loom Data Ingestion API (example)

The ingestion API includes endpoints such as:

- POST /data/network-flow - Ingests raw network flow data (binary payloads).
- POST /data/system-metrics - Ingests structured system metrics (JSON).

See docs/api/loom_data_api.yaml for the full OpenAPI spec.

## Local development

These are general instructions — adapt them to the language/framework used in the repository.

1. Install runtime (Python 3.11 recommended) and any language-specific toolchains.
2. Create a virtual environment and install dev dependencies if requirements-dev.txt exists:

   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-dev.txt

3. Lint and static checks

   - YAML linting: yamllint docs/api
   - OpenAPI validation: openapi-spec-validator (or similar)

4. Run tests

   pytest -q

5. Build (optional)

   If a Dockerfile is present you can build the image:

   docker build -t loom-origami:local .

## CI (GitHub Actions)

The repository includes a CI workflow at `.github/workflows/ci.yml`. The workflow is designed to be resilient: it only runs checks relevant to the repository contents and will skip steps when their inputs are missing.

Main checks performed:

- YAML linting of API specs in docs/api/
- OpenAPI validation of YAML files in docs/api/
- Python linting and tests (if a tests/ directory or pytest config is present)
- Docker build (if a Dockerfile exists)
- CodeQL analysis

The workflow is a good starting point — adapt the Python/Node/Go steps to your project's primary language.

## Contributing

Contributions are welcome. Please open an issue or PR describing your change. When modifying OpenAPI specs:

- Keep the specs in docs/api/.
- Ensure `yamllint` and OpenAPI validation pass before opening a PR.

## Notes and next steps

- If the repo has a primary language/runtime (Python/Go/Node), update the README Quickstart and CI to install and run that runtime's test and lint commands.
- Add contract/integration tests that exercise the OpenAPI specs against the running service (e.g., using schemathesis or a custom test harness).

# Build Stage
FROM ghcr.io/astral-sh/uv:python3.13-trixie-slim AS builder
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0

ARG PACKAGE
WORKDIR /app
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev --package="$PACKAGE"

COPY packages/"$PACKAGE" /app/packages/"$PACKAGE"
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-dev --package="$PACKAGE"

# Runtime Stage
FROM python:3.13-slim-trixie
ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app
COPY --from=builder --chown=app:app /app /app
CMD []

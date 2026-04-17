FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app

# Installer uv
RUN apt-get update \
    && apt-get install -y curl \
    && rm -rf /var/lib/apt/lists/* \
    && curl -LsSf https://astral.sh/uv/install.sh | sh \
    && ln -s /root/.local/bin/uv /usr/local/bin/uv

ENV UV_LINK_MODE=copy
ENV PATH="/app/.venv/bin:${PATH}"

EXPOSE 8000

# Le CMD est surchargé par compose.dev.yml / compose.prod.yml
CMD ["sh", "-c", "tail -f /dev/null"]

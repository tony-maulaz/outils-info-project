.PHONY: dev-up dev-down dev-logs dev-db prod-up prod-down prod-logs

# ─── Développement ────────────────────────────────────────────────────────────

dev-up:
	docker compose --env-file .env.dev -f compose.yml -f compose.dev.yml up --build

dev-down:
	docker compose --env-file .env.dev -f compose.yml -f compose.dev.yml down -v

dev-logs:
	docker compose --env-file .env.dev -f compose.yml -f compose.dev.yml logs -f --tail=100

# Initialiser (ou réinitialiser) la base de données avec les données de test
dev-db:
	docker compose --env-file .env.dev -f compose.yml -f compose.dev.yml exec backend \
		sh -c "uv run python -c 'from app.db import init_db; init_db()'"

# ─── Production ───────────────────────────────────────────────────────────────

prod-up:
	docker compose --env-file .env.prod -f compose.yml -f compose.prod.yml up -d --build

prod-down:
	docker compose --env-file .env.prod -f compose.yml -f compose.prod.yml down

prod-logs:
	docker compose --env-file .env.prod -f compose.yml -f compose.prod.yml logs -f --tail=100

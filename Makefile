.DEFAULT_GOAL := help

CONTAINER_PREFIX=moncifapp
DC=docker-compose -p ${CONTAINER_PREFIX}

setup: pull build up ## Setup the development environment

pull: ## Pull the external images
	${DC} pull

build: ## Build the containers and pull FROM statements
	${DC} build

rebuild: ## Rebuild containers
	${MAKE} down build up

up: ## Up the containers
	${DC} up -d

down: ## Down the containers (keep volumes)
	${DC} down

destroy: ## Destroy the containers, volumes, networks…
	${DC} down -v --remove-orphan

start: ## Start the containers
	${DC} start
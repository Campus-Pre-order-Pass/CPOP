.PHONY: show stop stop-rm docker-stop docker-run docker-build

show:
	docker ps

stop-all:
	docker stop $$(docker ps -q)

stop-rm:
	docker rm -f $$(docker ps -aq)


docker-build:
	docker-compose up --build

docker-run:
	docker-compose up

docker-down:
	docker-compose down
docker-rm:
	docker-compose down -v





IMAGE_NAME=project:1.0

up:
	docker-compose up --no-recreate

shell:
	docker-compose run --rm --service-ports web /bin/bash

clean:
	docker stop $$(docker ps -a -q)
	docker rm $$(docker ps -a -q)

build:
	docker build -t $(IMAGE_NAME) .

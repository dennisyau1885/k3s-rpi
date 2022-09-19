all: build run pause test stop

build:
	docker-compose build
run:
	docker run -d -p 5001:5000 \
		--env CONFIG=foo   \
		--name configis configis
pause:
	sleep 5
test:
	curl localhost:5001
stop:
	docker stop configis
	docker rm configis

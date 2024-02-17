build-dev:
	docker build -t dnd-dev -f Dockerfile.dev .
run-dev:
	docker run -it -d -v .:/code dnd-dev
build:
	docker build -t dnd .
run:
	docker run -it -v .:/code dnd
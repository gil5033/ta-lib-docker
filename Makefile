build:
	docker build -t ta-lib-docker:latest .

tag:
	docker tag ta-lib-docker:latest mkinney/ta-lib-docker:latest

push:
	docker push mkinney/ta-lib-docker:latest

test:
	./run_test.sh

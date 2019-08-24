IMG := emojinator
TAG := latest


docker-build:
	docker build --rm -t ${IMG}:${TAG} .


docker-run:
	docker run --rm -it --name ${IMG} -w /home -v `pwd`:/home ${IMG}:${TAG} /bin/ash


run:
	docker run --rm --name ${IMG} -w /home -v `pwd`:/home ${IMG}:${TAG} pipenv run python run.py

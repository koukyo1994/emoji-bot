IMG := emojinator
TAG := latest


docker-build:
	docker build --rm -t ${IMG}:${TAG} .


docker-run:
	docker run --rm -it --name ${IMG} -v `pwd`:/home ${IMG}:${TAG} /bin/ash

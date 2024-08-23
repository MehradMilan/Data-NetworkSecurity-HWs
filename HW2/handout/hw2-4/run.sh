docker build . -t login
docker run \
	-d \
	--rm \
	--name login \
	-p 8000:8000 \
	login


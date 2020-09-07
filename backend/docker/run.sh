APP=backend
PORT=5000
VERSION=latest
DOCKERFILE=./docker/Dockerfile
sudo docker build --build-arg PORT=$PORT -t $APP:$VERSION -f $DOCKERFILE . \
&& sudo docker run -it --publish $PORT:$PORT --volume "$PWD":/app --net=bridge $APP:$VERSION
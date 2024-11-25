# Define variables
IMAGE_NAME = shopping-list-app
DOCKER_USERNAME = fuyaoli

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run -p 8000:80 $(IMAGE_NAME)

# Remove the Docker image
clean:
	docker rmi $(IMAGE_NAME)

# List Docker images
image_show:
	docker images

# List running Docker containers
container_show:
	docker ps

# Push the image to Docker Hub
push:
	docker login
	docker tag $(IMAGE_NAME) $(DOCKER_USERNAME)/$(IMAGE_NAME)
	docker push $(DOCKER_USERNAME)/$(IMAGE_NAME):latest

# Log in to Docker Hub
login:
	docker login -u $(DOCKER_USERNAME)
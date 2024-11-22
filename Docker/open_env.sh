docker build -t tfgpu:2.9.1 .
docker run --gpus all -it -v $(pwd)/../:/tf/notebooks --network=host -p 8888:8888 tfgpu:2.9.1


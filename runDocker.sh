docker build -t fast-translate .
docker run -it --rm --runtime=nvidia -e NVIDIA_VISIBLE_DEVICES=all -p 9321:9321 fast-translate
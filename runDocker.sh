docker build -t fast-translate .
docker run -it --rm --runtime=nvidia -p 9321:9321 fast-translate
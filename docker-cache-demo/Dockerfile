from ubuntu:latest
WORKDIR /app
RUN apt-get update && apt-get install -y curl
COPY app.txt /app
CMD ["cat","/app/app.txt"]


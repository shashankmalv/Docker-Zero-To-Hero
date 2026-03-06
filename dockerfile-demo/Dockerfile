from nginx:latest
RUN apt-get update
WORKDIR /app
COPY index.html /usr/share/nginx/html
EXPOSE 80
# Default command when container starts
CMD ["nginx", "-g", "daemon off;"]
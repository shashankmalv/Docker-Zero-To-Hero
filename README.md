# Docker-Zero-To-Hero

Complete Docker roadmap: from beginner concepts (Zero) to advanced container orchestration and best practices (Hero).

## Overview

This repository contains hands-on examples and demonstrations covering Docker fundamentals, Docker Compose, multi-stage builds, and real-world applications. Each directory focuses on specific Docker concepts with practical implementations.

## Repository Structure

### Basic Docker Concepts

- **my-first-image/** - Introduction to creating your first Docker image
- **my-website/** - Simple static website containerization with Dockerfile and .dockerignore
- **dockerfile-demo/** - Dockerfile best practices and examples
- **cmd-demo/** - Understanding CMD instruction in Dockerfiles
- **entrypoint-demo/** - ENTRYPOINT vs CMD demonstration
- **docker-cache-demo/** - Docker layer caching optimization techniques

### Docker Compose

- **docker-compose/compose-basic/** - Basic Docker Compose setup
- **docker-compose/compose-env-demo/** - Environment variable management in Compose
  - `direct_env/` - Direct environment variable definition
  - `env_from_refrence/` - Environment variables from .env files
- **docker-compose/wordpress-compose/** - WordPress multi-container setup

### Multi-Stage Builds

- **Multistage-docker/large-image-demo/** - Optimizing image size with multi-stage builds
  - Comparison between single-stage and multi-stage Dockerfiles
  - Node.js application example

### Real-World Applications

- **3-tier-python-flsk-app/** - Three-tier Flask application with Docker Compose
  - Python Flask backend
  - Database integration
  - Multi-container orchestration

- **node-express-mongodb/** - Node.js + Express + MongoDB stack
  - RESTful API implementation
  - MongoDB integration
  - Environment configuration

- **flasky/** - Full-featured Flask blog application
  - User authentication and authorization
  - Database migrations with Alembic
  - API endpoints
  - Email functionality
  - Rich text posts and comments
  - Production-ready deployment configuration

### Additional Demos

- **nginx-bind-demo/** - Nginx volume binding demonstration

## Getting Started

### Prerequisites

- Docker installed on your system
- Docker Compose (for multi-container applications)
- Basic understanding of command line

### Running Examples

Each directory contains its own Dockerfile and/or docker-compose.yml. Navigate to any example directory and run:

```bash
# For single container applications
docker build -t <image-name> .
docker run -p <host-port>:<container-port> <image-name>

# For Docker Compose applications
docker-compose up -d
```

## Key Learning Topics

1. **Dockerfile Instructions** - CMD, ENTRYPOINT, COPY, ADD, WORKDIR
2. **Image Optimization** - Layer caching, multi-stage builds, .dockerignore
3. **Docker Compose** - Service orchestration, networking, volumes
4. **Environment Management** - Environment variables, .env files
5. **Real Applications** - Flask, Node.js, MongoDB, WordPress
6. **Best Practices** - Security, image size optimization, production deployments

## License

See LICENSE file for details.

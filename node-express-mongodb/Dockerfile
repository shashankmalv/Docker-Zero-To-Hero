#-----------stage 1:builder dependencies ------------
FROM node:20-alpine AS builder

WORKDIR /app

COPY package.json .

RUN npm install --omit=dev

COPY . .

#------------stage 2: production image-------------------

FROM node:20-alpine

# Create non-root user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

WORKDIR /app

COPY --from=builder /app /app

# Change ownership
RUN chown -R appuser:appgroup /app

# Switch to non-root user
USER appuser

# Expose application port
EXPOSE 8080

# Start application
CMD ["node", "server.js"]
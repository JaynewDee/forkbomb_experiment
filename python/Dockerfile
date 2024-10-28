# Use a lightweight image for building
FROM python:3.11-slim AS builder

# Set the working directory
WORKDIR /app

# Copy the fork bomb script into the container
COPY forkbomb.py .

# Use a minimal base image for the runtime
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy the fork bomb script from the builder stage
COPY --from=builder /app/forkbomb.py .

# Run the fork bomb
CMD ["python", "forkbomb.py"]

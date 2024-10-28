# Use a Golang image for building the application
FROM golang:latest AS builder

# Set the working directory
WORKDIR /app

# Copy the Go source code and go.mod into the container
COPY forkbomb.go .
COPY go.mod .

# Download the Go module dependencies (if any)
RUN go mod tidy

# Build the Go application
RUN go build -o forkbomb .

# Use a minimal base image for the runtime
FROM scratch

# Copy the compiled application from the builder stage
COPY --from=builder /app/forkbomb .

# Run the compiled application
CMD ["/forkbomb"]

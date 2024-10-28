# Use a builder image to compile C++
FROM gcc:latest AS builder

# Set the working directory
WORKDIR /usr/src/forkbomb

# Copy the C++ source file into the builder container
COPY forkbomb.cpp .

# Compile the C++ program
RUN g++ -static -o forkbomb forkbomb.cpp

# Minimal runtime stage
FROM scratch

# Copy the compiled binary from the builder stage
COPY --from=builder /usr/src/forkbomb/forkbomb /

# Run the compiled forkbomb binary
CMD ["/forkbomb"]

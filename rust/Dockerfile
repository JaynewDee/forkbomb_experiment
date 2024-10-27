# Use a builder image to compile rust for a linux target
FROM rust:latest as builder
WORKDIR /usr/src/forkbomb
COPY forkbomb .

# Build the application for the musl target
RUN rustup target add x86_64-unknown-linux-musl
RUN cargo build --release --target=x86_64-unknown-linux-musl

# Create a minimal runtime container for the bomb
FROM scratch
# Copy the compiled binary from the builder stage
COPY --from=builder /usr/src/forkbomb/target/x86_64-unknown-linux-musl/release/forkbomb .
# Execute
CMD ["./forkbomb"]

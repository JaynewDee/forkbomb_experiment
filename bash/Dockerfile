# Use a lightweight base image with Bash
FROM alpine:latest

# Install Bash (Alpine uses BusyBox by default)
RUN apk add --no-cache bash

# Copy script into image 
COPY forkbomb.sh /usr/local/bin/forkbomb

# Grant execute permissions 
RUN chmod +x /usr/local/bin/forkbomb

# Execute
CMD ["/usr/local/bin/forkbomb"]

# The Experiment
This project uses Docker to create containers designed to crash from the implementation of a fork bomb.  
Python scripting handles creation of images and containers for the respective language and measures the time it takes for a fork bomb script to crash the container.

## Requirements
- python3
- Docker

## Usage
1) Modify the `run.py` script at project root to point to your own python3 interpreter.
2) From project root: `./run.py <language> <mem_limit> <cpu_limit>`  
    - Only the `<language>` argument is required.
    - Optional: `<mem_limit>`
        - Examples: `100m`(100 MB) | `2g` (2 GB)  
    - Optional: `<cpu_limit>`
        - Examples: `1`(1 CPU Core) | `3`(3 CPU Cores)

## Helpful Commands

### Docker
#### Run a container in an interactive bash shell
> `docker run -it --entrypoint="bash" <image_name>`

#### Build docker image from Dockerfile
> `docker build -t <image_name> -f Dockerfile .`

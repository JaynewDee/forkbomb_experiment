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
        - Examples: `100m` (100 MB) | `2g` (2 GB)  
    - Optional: `<cpu_limit>`
        - Examples: `1` (1 CPU Core) | `3` (3 CPU Cores)
    
## Helpful Commands

### Docker
#### Run a container in an interactive bash shell
This is handy for troubleshooting errors with execution of the copied code
> `docker run -it --entrypoint="bash" <image_name>`

#### Build docker image from Dockerfile
> `docker build -t <image_name> -f Dockerfile .`

#### Examine stdout of a container
This is handy for confirming that the docker container failed as a result of the code itself and not something else such as a failure to execute.  
Uncomment the `remove_container(container_id)` line in `run.py` to keep the container alive after testing so that the container's id can be used to check the logs.
> `docker logs <container_id>`

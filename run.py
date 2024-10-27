#!/usr/bin/env python3

import signal
import sys

from lib import (
    run_command,
    print_available_languages,
    rebuild_image,
    time_container_run_duration,
    LANGUAGES
)

LANGUAGE = None
IMAGE_NAME = None 
MEMORY_LIMIT = "1g"
CPU_LIMIT = "1"

CONTAINER_ID = None


# Set up signal handling for graceful exit on Ctrl-C
def signal_handler(sig, frame):
    print("\nReceived exit signal (Ctrl-C)")
    if CONTAINER_ID:
        remove_container(CONTAINER_ID)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def start_container(img_name, mem, cpu) -> str:
    global CONTAINER_ID
    print(f"Starting container with image '{img_name}' ...")
    print(f"MEMORY LIMIT: {mem}")
    print(f"CPUS LIMIT: {cpu}")
    CONTAINER_ID = run_command(["docker", "run", "-d", "--memory", mem, "--cpus", cpu, img_name])
    print(f"CONTAINER ID: '{CONTAINER_ID}'")


def remove_container(id):
    global CONTAINER_ID
    run_command(["docker", "stop", id])
    run_command(["docker", "rm", id])
    CONTAINER_ID = None


def run():
    global LANGUAGE
    global IMAGE_NAME
    global MEMORY_LIMIT
    global CPU_LIMIT

    if len(sys.argv) < 2:
        print("Usage: python run.py <language> <memory_limit=1g> <cpus_limit=1>")
        print_available_languages()
        sys.exit(1)

    LANGUAGE = sys.argv[1]

    if LANGUAGE not in LANGUAGES:
        print_available_languages()
        sys.exit(1)

    IMAGE_NAME = f"{LANGUAGE}_fork_bomb"

    if (len(sys.argv) > 2):
        MEMORY_LIMIT = sys.argv[2]
    
    if (len(sys.argv) > 3):
        CPU_LIMIT = sys.argv[3]

    try:
        # build image
        rebuild_image(IMAGE_NAME, LANGUAGE)
        # start container
        start_container(IMAGE_NAME, MEMORY_LIMIT, CPU_LIMIT)
        # time duration container is alive
        runtime = time_container_run_duration(CONTAINER_ID)
        print(f"{LANGUAGE} fork bomb crashed the container in {runtime:.2f} seconds.")
    finally:
        if CONTAINER_ID:
            remove_container(CONTAINER_ID)


if __name__ == "__main__": run()

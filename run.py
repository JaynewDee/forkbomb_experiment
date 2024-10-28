#!/usr/bin/env python3

import signal
import subprocess
import sys
import threading
import time

from lib import (
    run_command,
    print_available_languages,
    rebuild_image,
    time_container_run_duration,
    monitor_container_stats,
    LANGUAGES
)

LANGUAGE = None
IMAGE_NAME = None 
MEMORY_LIMIT = "1g"
CPU_LIMIT = "1"

CONTAINER_ID = None

stats_thread = None
stop_event = threading.Event()  # Event to signal the monitoring thread

# Set up signal handling for graceful exit on Ctrl-C
def signal_handler(sig, frame):
    print("\nReceived exit signal (Ctrl-C)")
    if CONTAINER_ID:
        remove_container(CONTAINER_ID)

    stop_event.set()  # Signal the stats thread to stop
    if stats_thread:
        stats_thread.join()  # Wait for the stats thread to finish
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

def monitor_container_stats(container_id):
    """Run 'docker stats' command and display output."""
    try:
        # Run docker stats in a continuous loop until stop_event is set
        while not stop_event.is_set():
            # Use subprocess to call 'docker stats' with the container ID
            result = subprocess.run(
                ["docker", "stats", container_id, "--no-stream", "--format", "{{.Container}}\t{{.CPUPerc}}\t{{.MemUsage}}"],
                capture_output=True,
                text=True
            )
            print(result.stdout.strip())
            time.sleep(1)  # Delay between stats updates
    except KeyboardInterrupt:
        print("\nStopped monitoring container stats.")


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

        # Start monitoring container stats in a separate thread
        global stats_thread  # Make stats_thread global for access in the signal handler
        stats_thread = threading.Thread(target=monitor_container_stats, args=(CONTAINER_ID,))
        stats_thread.start()

        # time duration container is alive
        runtime = time_container_run_duration(CONTAINER_ID)
        print(f"{LANGUAGE} container crashed in {runtime:.2f} seconds.")
        exit_code = run_command(["docker", "inspect", CONTAINER_ID, "-f", "{{.State.ExitCode}}"])
        print(f"EXIT CODE: {exit_code}")
    finally:
        if CONTAINER_ID:
            pass
            # remove_container(CONTAINER_ID)
        stop_event.set()
        if stats_thread:
            stats_thread.join()


if __name__ == "__main__": run()

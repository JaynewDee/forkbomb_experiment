"""
A central location for any task-agnostic python code used by the project.
"""

import os
import subprocess
import sys
import time

LANGUAGES = ["rust", "powershell", "bash", "javascript"]


def print_available_languages():
    print("Available languages:")
    for l in LANGUAGES:
        print("     " + l)


def dockerpaths_by_language(lang):
    dir = os.path.join(os.getcwd(), lang)
    path = os.path.join(dir, "Dockerfile")
    return dir, path 


def run_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()


def check_image_exists(img_name):
    try:
        return run_command(["docker", "images", "-q", img_name])
    except SystemExit:
        return ""


def rebuild_image(img_name, lang):
    # Clean up old image if it exists
    if check_image_exists(img_name):
        # Clean up any existing containers first
        delete_containers_by_image(img_name)
        print(f"Removing old image '{img_name}'...")
        run_command(["docker", "rmi", img_name])
    # build image
    dir, path = dockerpaths_by_language(lang)
    run_command(["docker", "build", "-t", img_name, "-f", path, dir])
    print(f"Image '{img_name}' built successfully.")


def delete_containers_by_image(img_name):
    print(f"Stopping and removing containers created from image '{img_name}'...")

    # Stop running containers created from the specified image
    stop_command = f"docker ps -q --filter ancestor={img_name}".split()
    try:
        running_containers = subprocess.check_output(stop_command).decode().splitlines()
        if running_containers:
            subprocess.run(["docker", "stop"] + running_containers, check=True)
    except subprocess.CalledProcessError:
        print("No running containers found to stop.")

    # Remove all containers created from the specified image
    rm_command = f"docker ps -aq --filter ancestor={img_name}".split()
    try:
        all_containers = subprocess.check_output(rm_command).decode().splitlines()
        if all_containers:
            subprocess.run(["docker", "rm"] + all_containers, check=True)
    except subprocess.CalledProcessError:
        print("No containers found to remove.")

    print("Containers deleted.")


def delete_image(img_name):
    run_command(["docker", "rmi", img_name]) 


def time_container_run_duration(container_id):
    # Time the duration that container is in "running" state
    start_time = time.time() 
    while True:
        running_state = run_command(["docker", "inspect", "-f", "{{.State.Running}}", container_id])
        print("Container is running ... ")
        if running_state != "true":
            break
        time.sleep(0.1)
    end_time = time.time()
    return end_time - start_time

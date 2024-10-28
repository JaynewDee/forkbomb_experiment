#!/usr/bin/env python3
"""
A convenience script for cleaning up any images and containers used by the project.

The <language>_fork_bomb image-naming convention makes this possible.

Usage: `./cleanup.py`
"""

from lib import (
    check_image_exists,
    delete_containers_by_image, 
    delete_image,
    LANGUAGES
)

def cleanup():
    images = [lang + "_fork_bomb" for lang in LANGUAGES]

    for img in images:
        if check_image_exists(img):
            delete_containers_by_image(img)
            delete_image(img)


if __name__ == "__main__": cleanup()

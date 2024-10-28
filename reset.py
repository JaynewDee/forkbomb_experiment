#!/usr/bin/env python3
"""
A convenience script for cleaning up any images and containers used by the project.

The <language>_fork_bomb image-naming convention makes this possible.

Usage: `./reset.py`
"""

from lib import (
    delete_containers_by_image, 
    delete_image,
    LANGUAGES
)

def reset():
    images = [lang + "_fork_bomb" for lang in LANGUAGES]

    for img in images:
        delete_containers_by_image(img)
        delete_image(img)


if __name__ == "__main__": reset()

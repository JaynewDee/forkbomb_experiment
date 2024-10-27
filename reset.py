#!/usr/bin/env python3

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

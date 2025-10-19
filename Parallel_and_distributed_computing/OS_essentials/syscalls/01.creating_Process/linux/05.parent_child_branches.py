import os

def main():
    pid = os.fork()

    if pid == 0:
        print(f"👶 Child: PID={os.getpid()}, PPID={os.getppid()}")
    else:
        print(f"🧑 Parent: PID={os.getpid()}, Child PID={pid}")

if __name__ == "__main__":
    main()

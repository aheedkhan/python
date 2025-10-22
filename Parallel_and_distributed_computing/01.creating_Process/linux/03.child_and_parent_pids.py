import os

def main():
    pid = os.fork()

    if pid == 0:
        print(f"Child process → PID: {os.getpid()}, Parent PID: {os.getppid()}")
    else:
        print(f"Parent process → PID: {os.getpid()}, Child PID: {pid}")

if __name__ == "__main__":
    main()

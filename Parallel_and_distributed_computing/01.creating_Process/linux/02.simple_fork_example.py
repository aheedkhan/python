import os

def main():
    pid = os.fork()  # Duplicates the current process

    print("PID returned by fork:", pid)
    print("My actual process ID:", os.getpid())

if __name__ == "__main__":
    main()


# it will run 2 times because fork creates a new process
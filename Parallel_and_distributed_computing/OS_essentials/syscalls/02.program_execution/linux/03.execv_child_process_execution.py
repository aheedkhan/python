#parent for program "03.child_program.py" & execution using execv
import os

def main():
    pid = os.fork()
    if pid == 0:
        msg = input("send msg to new program as arg:")

        # without arguments
        # os.execv("/usr/bin/python3", "haha (process name)", "03.child_program.py")

        # with arguments
        os.execv("/usr/bin/python3",["hwhw (process name)", "03.child_program.py",msg,f"pid as arg from parent {os.getpid()}"])
    else:
        print("parent: waiting for child process to complete after user input 5secs...")
        os.wait()
        print(f"i m parent {os.getpid()}")


if __name__ == "__main__":
    main()
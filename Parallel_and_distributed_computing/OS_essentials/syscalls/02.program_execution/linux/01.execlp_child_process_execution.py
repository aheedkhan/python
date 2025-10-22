#parent for program "01.child_program.py" & execution using execlp
import os


def main():
    pid = os.fork()
    
    if pid == 0:
        msg = input("send msg to new program as arg:")
        # without arguments
        # os.execlp("python3", "haha (process name)", "01.child_program.py")

        # with arguments
        os.execlp("python3", "haha (process name)", "01.child_program.py", msg, f"pid as arg from parent {os.getpid()}")
    else:
        print("parent: waiting for child process to complete after user input 5secs...")
        os.wait()
        print("i m parent", os.getpid())

if __name__ == "__main__":
    main()

# While parent waits use ps -aux in terminal to see child process name
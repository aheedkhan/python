#parent for program "02.child_program.py" & execution using execl
import os

def main():
    pid = os.fork()
    if pid == 0:
        msg = input("send msg to new program as arg:")

        # without arguments
        # os.execl("/usr/bin/python3", "haha (process name)", "02.child_program.py")

        # with arguments
        os.execl("/usr/bin/python3","hwhw (process name)","02.child_program.py",msg,f"pid as arg from parent {os.getpid()}")
    else:
        print("parent: waiting for child process to complete after user input 5secs...")
        os.wait()
        print(f"i m parent {os.getpid()}")



if __name__ == "__main__":
    main()

# While parent waits use ps -aux in terminal to see child process name
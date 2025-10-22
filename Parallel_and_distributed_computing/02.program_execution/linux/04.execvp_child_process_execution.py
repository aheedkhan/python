#parent for program "08.with_arg_child_program.py" & execution using execvp

import os

def main():
    pid = os.fork()
    if pid == 0:
        msg = input("Enter a message to pass to the child process: ")

        # without arguments
        # os.execvp("python3", "haha (process name)", "03.child_program.py")

        # with arguments
        os.execvp("python3", ["huhu (process name)", "04.child_program.py", msg,f"pid as arg from parent {os.getpid()}"])
    else:
        print("parent: waiting for child process to  complete after user input 5secs...")
        os.wait()
        print(f"i m parent {os.getpid()}")

if __name__ == "__main__":
    main()
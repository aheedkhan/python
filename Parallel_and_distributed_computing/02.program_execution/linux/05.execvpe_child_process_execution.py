import os 


def main():
    pid = os.fork()
    if pid == 0:

        msg = input("Enter a message for child process: ")
        env = os.environ.copy()
        env[Path]
        # without arguments
        #os.execvpe("python3",["huhu (process name)", "05.child_program.py"], os.environ)
        # with arguments
        os.execvpe("python3",["hello (process name)", "05.child_program.py", msg, f"pid as arg from parent {os.getpid()}"], env)

#in progess
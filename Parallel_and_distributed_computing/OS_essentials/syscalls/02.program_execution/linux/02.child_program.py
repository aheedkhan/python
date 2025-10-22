import os, time

def main():
    print("i m child and my pid inside script", os.getpid())

    # without arguments
    # print("No args passed to me")

    # with arguments
    arg = os.sys.argv[0:]
    print("Msg recived in args:", arg[1])
    print("Arguments passed to me:", os.sys.argv[0:])
    time.sleep(5)


if __name__ == "__main__":
    main()
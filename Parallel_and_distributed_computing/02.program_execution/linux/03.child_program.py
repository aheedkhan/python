import os, time

def main():
    print(f"i m child {os.getpid()}")
    # without arguments
    # print("No args passed to me")


    # with arguments
    msg = os.sys.argv[1]
    print(f"Msg recived in args: {msg}")
    print(f"Arguments passed to me: {os.sys.argv[0:]}")
    time.sleep(5)


if __name__ == "__main__":
    main()

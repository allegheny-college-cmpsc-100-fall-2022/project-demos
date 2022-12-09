import os, signal

def main():
    os.kill(os.getppid(), signal.SIGHUP)

if __name__ == "__main__":
    main()
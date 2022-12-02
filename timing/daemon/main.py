from Tick import Tick
from time import sleep

def main():

    t = Tick(5)

    while True:
        print(".")
        sleep(1)
        is_elapsed = t.elapsed()
        if is_elapsed:
            t = Tick(5)

if __name__ == "__main__":
    main()
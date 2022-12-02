from time import sleep
from Tick import Tick

def main():

    t = Tick(10)
    count = 1

    while True:
        print(f"{count}")
        sleep(1)
        is_elapsed = t.elapsed()
        if is_elapsed:
            break
        count += 1

if __name__ == "__main__":
    main()
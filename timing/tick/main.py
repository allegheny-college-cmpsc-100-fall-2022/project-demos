from time import sleep
from Tick import Tick

def main():

    t = Tick()
    
    timestamp = t.now()
    count = 1

    while True:
        print(f"{count}")
        sleep(1)
        is_elapsed = t.elapsed(timestamp, 10)
        if is_elapsed:
            break
        count += 1

if __name__ == "__main__":
    main()
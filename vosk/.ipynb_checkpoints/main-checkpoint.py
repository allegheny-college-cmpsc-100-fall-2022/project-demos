import os
import Translator

def main():
    files = os.listdir("wav")
    for file in files:
        text = Translator.transcribe(f"wav/{file}")
        print(f"FINAL TEXT: {text}")

if __name__ == "__main__":
    main()

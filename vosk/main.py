import os
import Translator

def main():
    files = os.listdir("wav")
    for file in files:
      print(f"[{files.index(file) + 1}]\t{file}")
    choice = int(input("Which number? "))
    text = Translator.transcribe(f"wav/{files[choice - 1]}")
    print(f"FINAL TEXT: {text}")

if __name__ == "__main__":
    main()

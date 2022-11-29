import Translator

def main():
    text = Translator.transcribe("wav/QuickFox.wav")
    print(f"FINAL TEXT: {text}")

if __name__ == "__main__":
    main()

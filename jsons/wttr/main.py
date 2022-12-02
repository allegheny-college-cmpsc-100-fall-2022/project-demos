import json
import requests

def main():
    # To write to file, python main.py > data
    city = "Meadville"
    request = requests.get(
        f"https://wttr.in/{city}?format=j1"
    )
    data = json.loads(request.text)

    print(json.dumps(data, indent = 4))

if __name__ == "__main__":
    main()
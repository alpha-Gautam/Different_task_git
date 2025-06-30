import requests
import random
num=random.randint(1, 100)
print(f"Random number generated: {num}")

url = f"https://api.freeapi.app/api/v1/public/randomjokes/{num}"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)
data=response.json()
response_data=data["data"]["content"]
print(f"Response data length from API: {len(response_data)}")


with open("jokes.txt", "a") as f:
    print(f.readable())
    try:
        f.write(response_data+"\n")
        print("Jokes  saved in jokes.txt\n")
        print(f"Joke: {response_data}")
        
    except Exception as e:
        print(f"Error occurred while writing to file: {e}")
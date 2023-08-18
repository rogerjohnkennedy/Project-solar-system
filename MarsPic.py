import requests
import random

def get_mars_image(api_key):
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {
        "sol": random.randint(100, 2000),  # Choose a random sol (Martian day)
        "api_key": api_key,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "photos" in data and len(data["photos"]) > 0:
        random_photo = random.choice(data["photos"])
        return random_photo["img_src"]
    else:
        return None

def main():
    # Replace with your Personal Key in the place {API KEY} NASA API key
    # You will get the key for https://api.nasa.gov/
    nasa_api_key = "API KEY"

    image_url = get_mars_image(nasa_api_key)
    if image_url:
        print("Random Mars Image URL:", image_url)
    else:
        print("No images found.")

if __name__ == "__main__":
    main()

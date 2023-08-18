import requests
import random
from PIL import Image
from io import BytesIO

def get_mars_image(api_key):
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    params = {
        "sol": random.randint(100, 2000),
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
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content
            image = Image.open(BytesIO(image_data))
            image.show()
        else:
            print("Failed to fetch image.")
    else:
        print("No images found.")

if __name__ == "__main__":
    main()

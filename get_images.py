import requests
import json
from PIL import Image

data = {}
with open("data/cards.json", 'r') as file:
    data = json.load(file)

for group in ["A1", "A1a", "A2", "P-A"]:
    pack_cards = data[group]
    for id, info in pack_cards.items():
        img_url = info["img"]
        r = requests.get(img_url)

        with open(f"images/{group}/{id}.jpg", 'wb') as save_image:
            save_image.write(r.content)

        with Image.open(f"images/{group}/{id}.jpg") as img:
            my_image = img.resize((img.width, img.height), Image.LANCZOS).convert("RGB")
            my_image.save(f"images/{group}/{id}.jpg")
        

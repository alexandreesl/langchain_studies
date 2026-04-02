from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper
dalle = DallEAPIWrapper(model="dall-e-3",size="1024x1024",       # Image dimensions
    quality="hd",  )
# Generate an image
image_url = dalle.run("A robot cyberpunk girl with a green hair on city night, on top of a motorcycle. Should be a high quality image, cyberpunk 2077 style.")
# Display the image in a notebook
from IPython.display import Image, display
display(Image(url=image_url))
# Or save it locally
import requests
response = requests.get(image_url)
with open("image.png", "wb") as f:
    f.write(response.content)

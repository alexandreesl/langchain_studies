from langchain_community.llms import Replicate
# Initialize the text-to-image model with Stable Diffusion 3.5 Large
text2image = Replicate(
    model="stability-ai/stable-diffusion-3.5-large",
    model_kwargs={
        "prompt_strength": 0.85,
        "cfg": 4.5,
        "steps": 40,
        "aspect_ratio": "1:1",
        "output_format": "webp",
        "output_quality": 90
    }
)
# Generate an image
image_url = text2image.invoke(
    "A cyberpunk girl with a green hair on city night, on top of a motorcycle. Should be a high quality image, cyberpunk 2077 style."
)
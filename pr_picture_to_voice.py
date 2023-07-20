from transformers import pipeline
import os

os.environ["HUGGINGFACEHUB_API_TOKEN"] = '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'

# img2text
def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

    text = image_to_text(url)[0]["generated_text"]

    print(text)
    return text

img2text("m.png")

# llm
import openai
from dotenv import load_dotenv
import os

load_dotenv()

# set openai.api_key to your api key
openai.api_key = os.getenv('OPENAI_API_KEY')


response = openai.images.generate(
  model="dall-e-3",
  prompt="The luminous bardo of dharmata",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url

print(image_url)
print(' ')
print(type(response))
print(response)


import os
import openai
from dotenv import load_dotenv

load_dotenv()

I = str(input('Please input Image Name: '))

openai.organization = "org-gv3yWWCUbdcDMU1vO1mDzxnW"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

model = openai.Image.create_variation(
    image = open('temp/' + I, 'rb'),
    n = 1,
    size = '512x512',
)

image_url = model['data'][0]['url']
print(image_url)
with open('VariationResult.txt', 'w+') as r:
    for i in model.data:
        r.write(image_url + '\n')
r.close()
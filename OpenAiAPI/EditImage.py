import os
import openai
from dotenv import load_dotenv

load_dotenv()

I = str(input('Please input Image Name: '))
m = str(input('Please input Image Name: '))
p = str(input('Please input a prompt: '))

openai.organization = "org-gv3yWWCUbdcDMU1vO1mDzxnW"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.list()

model = openai.Image.create_edit(
    image = open('temp/' + I, 'rb'),
    mask = open('temp/' + m, 'rb'),
    prompt=p,
    n = 1,
    size = '512x512',
)

with open('EditResult.txt', 'w+') as r:
    for i in model.data:
        r.write(str(i).replace('{', '').replace('}', '').replace('"url":', '').replace('"', '').strip() + '\n')
r.close()

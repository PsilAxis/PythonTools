## Create a .env file with your OPENAI_API_KEY inside. This is needed for Ai.py.
## Get your keys here - https://beta.openai.com/account/api-keys

## Ai.py is used to connect to the OpenAi Api and use your own custom prompt to generate ai art and creates a txt file with all the new links called result.txt
## GifMaker.py is used to take all the link from the result.txt file and make a gif file out of it that is saved to the current folder, with the name my_gif.gif.

## Both.py imports the Ai.py and GifMaker.py scripts and uses both of them in a single run.

## Variation.py creates a variation of the chosen image.

## EditImage.py creates an edit of an image using a mask. this requires a mask image. 'ie. mask.png'

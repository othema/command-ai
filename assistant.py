import openai
import dotenv
from os import getenv

dotenv.load_dotenv(".env")
api_key = getenv("API_KEY")
api_base = getenv("API_BASE")
model = getenv("MODEL")

API_BASE = "https://api.pawan.krd/v1"  # https://api.openai.com/v1
HEADERS = {
	"Authorization": "Bearer " + api_key,
	"Content-Type": "application/json"
}


openai.api_key = api_key
openai.api_base = api_base


def ask(message, system = "", model=model):
	completion = openai.ChatCompletion.create(
		model=model,
		messages=[
			{
				"role": "system",
				"content": system
			},
			{
					"role": "user",
					"content": message
			}
		]
	)
	return completion.choices[0].message.content

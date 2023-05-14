# Command AI
A Github Copilot for CLI clone. Works on **any** operating system.

## Examples
![Example 1](https://user-images.githubusercontent.com/78880488/238178855-78ded997-0a1d-463c-8793-3a026d573c73.png)
![Example 2](https://user-images.githubusercontent.com/78880488/238178926-d7843136-6350-41bd-86e8-2ad80c99ae3d.png)

## Setup
1. Clone the project `git clone https://github.com/othema/command-ai.git`
1. `cd` to the project directory, and create a `.env` file
1. Add this data to the `.env` file:
	```env
	API_KEY = <YOUR_API_KEY>
	API_BASE = https://api.openai.com/v1  # To allow for proxies
	MODEL = gpt-3.5-turbo  # Or choose any other model
	```
	The `API_BASE` key allows for proxy configuration, for example if you are not willing to pay for the OpenAI API key. If you are interested, take a look at [this proxy](https://github.com/PawanOsman/ChatGPT) to use this project for free.
1. Install the requirements `pip install -r requirements.txt`

## Usage
**Basic usage:** `python main.py <prompt>`
<br />
You can setup an alias in your `.bashrc` to allow for usage in any directory, for example (in Linux/MacOS):
```bash
alias ai="python /path/to/code/main.py"
```
This allows for usage like this from any directory: `ai <prompt>`
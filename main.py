import assistant
import sys
from beaupy import select, spinners
from os import system

SYSTEM = "I want you to act like a CMD translator. I will give you a description of the command in english, and you will translate that into a CMD command for Windows. Do not provide any explanations. Do not respond with anything except the command"

def main():
  try:
    prompt = " ".join(sys.argv[1:])
    command = generate_command(prompt)
    if command:
      system(command)
    else:
      print("❌ Cancelled")
  except KeyboardInterrupt:
    print("❌ Cancelled")


def generate_command(prompt):
  loader = spinners.Spinner(spinners.CLOCK, "Asking ChatGPT...")

  loader.start()
  command = assistant.ask(prompt, SYSTEM)
  loader.stop()

  print("\033[1m" + command + "\033[0m")
  action = select(["✅ Run this command", "📝 Revise query", "❌ Cancel"]).lower()

  if action == "✅ run this command":
      return command
  elif action == "📝 revise query":
    revision_prompt = input("Revision: ")
    return generate_command(f"Change this command: {command}\nwith these edits: {revision_prompt}")
  else:
    return None


main()

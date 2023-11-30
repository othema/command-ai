import assistant
import sys
from beaupy import select, spinners
import os
import platform


def main():
  operating_system = platform.system() + " " + platform.release()
  dirname = os.path.abspath(os.path.dirname(__file__))

  os_replace = lambda x: x.replace("{OPERATING_SYSTEM}", operating_system)

  with open(os.path.join(dirname, "prompts/command.txt")) as f:
    system_command = os_replace(f.read())
  with open(os.path.join(dirname, "prompts/explain.txt")) as f:
    system_explain = os_replace(f.read())

  try:
    prompt = " ".join(sys.argv[1:])
    command = generate_command(prompt, system_command, system_explain)
    if command:
      os.system(command)
    else:
      print("❌ Cancelled")
  except KeyboardInterrupt:
    print("❌ Cancelled")
  except AttributeError:
    print("❌ Cancelled")


def generate_command(prompt, system_command="", system_explain=""):
  loader = spinners.Spinner(spinners.CLOCK, "Asking ChatGPT...")

  loader.start()
  command = assistant.ask(prompt, system_command)
  explanation = syntax_highlight(assistant.ask(command, system_explain))
  loader.stop()

  print("\n\033[1m" + syntax_highlight(command, "\33[33m") + "\033[0m\n")
  print(explanation + "\n")
  action = select(["✅ Run this command", "📝 Revise query", "❌ Cancel"]).lower()

  if action == "✅ run this command":
      return command
  elif action == "📝 revise query":
    revision_prompt = input("Revision: ")
    return generate_command(f"Change this command: {command}\nwith these edits: {revision_prompt}", system_command, system_explain)
  else:
    return None


def syntax_highlight(text, color="\33[94m"):
  return text.replace("{STARTH}", color).replace("{ENDH}", "\033[0m")


main()

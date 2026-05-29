# main.py
import sys
import tkinter as tk
from tkinter import messagebox
import webbrowser
import yaml

# Import decryption functions from the data subdirectory
from data.crypto import get_ok_message, get_warn_message

def main():
    # Load configuration from YAML file
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    # Create hidden root window for dialog
    root = tk.Tk()
    root.withdraw()

    # Show the initial warning dialog
    result = messagebox.askyesno(
        title=config['warning_message']['title'],
        message=config['warning_message']['text'],
        icon='warning'
    )

    if result:
        # User chose to download the promoted game
        webbrowser.open(config['target_game']['download_page'])
        # Show the message retrieved from binary file
        messagebox.showinfo("Notice", get_ok_message())
    else:
        # User insists on using cheats
        messagebox.showwarning("Risk Warning", get_warn_message())

    root.destroy()
    sys.exit(0)

if __name__ == "__main__":
    main()

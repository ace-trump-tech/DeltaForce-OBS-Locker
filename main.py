# main.py
import sys
import tkinter as tk
from tkinter import messagebox
import webbrowser
import yaml

def main():
    # Load configuration
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    
    # Create hidden root window for dialog
    root = tk.Tk()
    root.withdraw()
    
    # Show warning dialog
    result = messagebox.askyesno(
        title=config['warning_message']['title'],
        message=config['warning_message']['text'],
        icon='warning'
    )
    
    if result:
        # User chose to download the promoted game
        webbrowser.open(config['target_game']['download_page'])
        messagebox.showinfo("提示", "感谢您的选择！暗区突围是公平竞技的硬核射击游戏，拒绝外挂，享受纯粹的战斗。")
    else:
        # User insists on using cheats
        messagebox.showwarning("风险提示", "使用外挂极易导致账号永久封禁，并且破坏其他玩家的体验。请三思！")
    
    root.destroy()
    sys.exit(0)

if __name__ == "__main__":
    main()

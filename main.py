import pyautogui
import random
import time
import keyboard
import pydirectinput
import os
import tkinter as tk
from tkinter import ttk
import threading

pyautogui.FAILSAFE = True

class Settings:
    def __init__(self):
        self.buy_x = 960
        self.buy_y = 540
        self.click_speed = 0.1
        self.move_time = 0.5
        self.move_delay = 60
        self.running = False
        self.stop_flag = False

settings = Settings()

def release_all_keys():
    for key in ['w', 'a', 's', 'd', 'space']:
        try:
            pydirectinput.keyUp(key)
        except:
            pass

def walk_cycle():
    if settings.stop_flag:
        return
    
    release_all_keys()
    time.sleep(0.05)
    
    pydirectinput.keyDown('w')
    time.sleep(settings.move_time)
    pydirectinput.keyUp('w')
    time.sleep(0.15)
    
    pydirectinput.keyDown('s')
    time.sleep(settings.move_time)
    pydirectinput.keyUp('s')
    time.sleep(0.15)
    
    release_all_keys()

def spam_click():
    offset_x = random.randint(-2, 2)
    offset_y = random.randint(-2, 2)
    pyautogui.click(settings.buy_x + offset_x, settings.buy_y + offset_y)

def farm_loop():
    release_all_keys()
    last_move = time.time()
    
    while settings.running and not settings.stop_flag:
        try:
            spam_click()
            time.sleep(settings.click_speed)
            
            if time.time() - last_move >= settings.move_delay and not settings.stop_flag:
                walk_cycle()
                last_move = time.time()
        except:
            break
    
    release_all_keys()
    settings.running = False
    settings.stop_flag = False
    root.after(0, reset_ui)

def reset_ui():
    if app:
        app.toggle_btn.config(text="Start (F6)", bg="#4caf50")
        app.status_label.config(text="Idle")

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("GAG2 Afker")
        self.root.geometry("320x280")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        title = tk.Label(root, text="GAG2 Afker", font=("Segoe UI", 14, "bold"), 
                        fg="#ffffff", bg="#1e1e1e")
        title.pack(pady=(15, 5))
        
        settings_frame = tk.Frame(root, bg="#1e1e1e")
        settings_frame.pack(pady=10)
        
        tk.Label(settings_frame, text="Click Speed (sec):", fg="white", bg="#1e1e1e", 
                font=("Segoe UI", 10)).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.speed_var = tk.StringVar(value="0.1")
        tk.Entry(settings_frame, textvariable=self.speed_var, width=8, 
                font=("Segoe UI", 10)).grid(row=0, column=1, padx=10, pady=5)
        
        tk.Label(settings_frame, text="Move Time (sec):", fg="white", bg="#1e1e1e", 
                font=("Segoe UI", 10)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.move_var = tk.StringVar(value="0.5")
        tk.Entry(settings_frame, textvariable=self.move_var, width=8, 
                font=("Segoe UI", 10)).grid(row=1, column=1, padx=10, pady=5)
        
        tk.Label(settings_frame, text="Move Delay (sec):", fg="white", bg="#1e1e1e", 
                font=("Segoe UI", 10)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.delay_var = tk.StringVar(value="60")
        tk.Entry(settings_frame, textvariable=self.delay_var, width=8, 
                font=("Segoe UI", 10)).grid(row=2, column=1, padx=10, pady=5)
        
        self.toggle_btn = tk.Button(root, text="Start (F6)", font=("Segoe UI", 11, "bold"),
                                   bg="#4caf50", fg="white", width=20, height=2, command=self.toggle)
        self.toggle_btn.pack(pady=(15, 5))
        
        self.status_label = tk.Label(root, text="Idle - Hover mouse, press F6", fg="#888888", 
                                    bg="#1e1e1e", font=("Segoe UI", 9))
        self.status_label.pack(pady=(0, 10))
        
        keyboard.add_hotkey('f6', self.toggle)
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def toggle(self):
        if settings.running:
            settings.running = False
            settings.stop_flag = True
            release_all_keys()
            self.toggle_btn.config(text="Start (F6)", bg="#4caf50")
            self.status_label.config(text="Stopped")
        else:
            try:
                settings.click_speed = float(self.speed_var.get())
                settings.move_time = float(self.move_var.get())
                settings.move_delay = float(self.delay_var.get())
            except ValueError:
                self.status_label.config(text="Invalid settings")
                return
            
            x, y = pyautogui.position()
            settings.buy_x = x
            settings.buy_y = y
            
            settings.running = True
            settings.stop_flag = False
            release_all_keys()
            self.toggle_btn.config(text="Stop (F6)", bg="#f44336")
            self.status_label.config(text=f"Running at {x}, {y}")
            
            thread = threading.Thread(target=farm_loop, daemon=True)
            thread.start()
    
    def on_close(self):
        settings.running = False
        settings.stop_flag = True
        release_all_keys()
        self.root.destroy()
        os._exit(0)

app = None

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

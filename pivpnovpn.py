import tkinter as tk
import pexpect
import threading
import signal

child = None

def connect_vpn():
    global child
    child = pexpect.spawn('sudo openvpn /file path/to/your file name.ovpn') # Your ovpn file path and file name
    child.expect('password for XXXX:') #
    child.sendline('xxxxx')  # Your sudo password replace only the xxxxx
    child.expect('Enter Private Key Password:')
    child.sendline('xxxxx')  # Your private key password replace only the xxxxx
    child.interact()  # This allows you to interact with the process

def disconnect_vpn():
    global child
    if child is not None:
        child.kill(signal.SIGINT)

def update_status():
    threading.Thread(target=connect_vpn).start()

root = tk.Tk()
root.title("VPN Connection")
root.geometry("500x300")  # Set window size
root.configure(bg='black')  # Set dark background

connect_button = tk.Button(root, text="Connect", command=update_status, bg='grey', fg='white')
connect_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Fill the window and add padding

disconnect_button = tk.Button(root, text="Disconnect", command=disconnect_vpn, bg='grey', fg='white')
disconnect_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)  # Fill the window and add padding

root.mainloop()
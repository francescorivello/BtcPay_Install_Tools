import tkinter as tk
from tkinter import filedialog
import paramiko

def connect_ssh(hostname, username, password, key_file, key_passphrase):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        if key_file:
            private_key = paramiko.RSAKey(filename=key_file, password=key_passphrase)
            client.connect(hostname, username=username, pkey=private_key)
        else:
            client.connect(hostname, username=username, password=password)

        return client
    except Exception as e:
        print(f"Error while estabilishing connection: {e}")
        return None

def select_script():
    script_path = filedialog.askopenfilename(filetypes=[("Script Shell", "*.sh")])
    script_path_entry.delete(0, tk.END)
    script_path_entry.insert(0, script_path)

def select_key_file():
    key_file_path = filedialog.askopenfilename(filetypes=[("SSH key", "*pem")])
    key_file_entry.delete(0, tk.END)
    key_file_entry.insert(0, key_file_path)

def start_installation():
    hostname = hostname_entry.get()
    key_file = key_file_entry.get()
    key_passphrase = key_passphrase_entry.get()
    password = password_entry.get()
    username = username_entry.get()
    local_script_path = script_path_entry.get()

    if not hostname:
        print("Insert remote server ip address.")
        return

    if not local_script_path:
        print("Chose the directory of install script.")
        return

    client = connect_ssh(hostname, username, password, key_file, key_passphrase)
    if client:
        remote_script_path = "install.sh"

        try:
            with open(local_script_path, 'r') as local_script_file:
                script_contents = local_script_file.read()
            with client.open_sftp() as sftp:
                with sftp.file(remote_script_path, 'w') as remote_script_file:
                    remote_script_file.write(script_contents)

            _, stdout, stderr = client.exec_command(f"chmod +x {remote_script_path}")
            _, stdout, stderr = client.exec_command(f"./{remote_script_path}")
            print(stdout.read().decode('utf-8'))
            print(stderr.read().decode('utf-8'))
            print("Successfully installed.")
            finish_label = tk.Label(window, text="Successfully installed.")
            finish_label.pack()

        except Exception as e:
            print(f"Error while sending script: {e}")
            finish_label = tk.Label(window, text=f"Error while sending script: {e}")
            finish_label.pack()

        client.close()

#windows
window = tk.Tk()
window.title("BtcPay install tools remote installer")
window.geometry("450x400")

# Labels and input
hostname_label = tk.Label(window, text="Remote server IP:")
hostname_label.pack()
hostname_entry = tk.Entry(window)
hostname_entry.pack()

key_file_label = tk.Label(window, text="Private ssh key(Leave blank if not necessary):")
key_file_label.pack()
key_file_entry = tk.Entry(window)
key_file_entry.pack()

key_passphrase_label = tk.Label(window, text="Passphrase private key (Leave blank if not necessary):")
key_passphrase_label.pack()
key_passphrase_entry = tk.Entry(window, show="*")
key_passphrase_entry.pack()

username_label = tk.Label(window, text="Username to use:")
username_label.pack()
username_entry = tk.Entry(window, show="*")
username_entry.pack()

script_path_label = tk.Label(window, text="Install script directory:")
script_path_label.pack()
script_path_entry = tk.Entry(window)
script_path_entry.pack()

password_label = tk.Label(window, text="Password:(Leave blank if using private key auth)")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

#Buttons
browse_script_button = tk.Button(window, text="Chose install script", command=select_script)
browse_script_button.pack()

browse_key_file_button = tk.Button(window, text="Chose private key", command=select_key_file)
browse_key_file_button.pack()


start_button = tk.Button(window, text="Start Installation", command=start_installation)
start_button.pack()

window.mainloop()

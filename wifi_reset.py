import shutil
import paramiko
from os import path
from env import *


def restart_wifi():
    if i_am == "pi":
        path_to_file = "/home/pi/.ssh/{}".format(file_name)
    else:
        path_to_file = "/Users/{}/.ssh/{}".format(i_am, file_name)

    if not path.exists(file_name):
        shutil.copy(path_to_file, ".")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=password, timeout=10)
    ssh.exec_command(reboot_command)
    ssh.close()

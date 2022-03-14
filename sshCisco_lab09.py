#script to connect to Cisco device via SSH

import datetime
import pathlib
import os
import netmiko

from pathlib import Path
from netmiko import ConnectHandler
from getpass import getpass

#lab09 Additions
from netmiko.ssh_exception import AuthenticationException, SSHException, NetMikoTimeoutException


USERNAME = input("Please enter your SSH username: ")
PASS = getpass("Please enter your SSH password: ")

myPath = Path.cwd()

d = datetime.datetime.now()

fileName = 'csrBackup'

fileExt = '.txt'

backup = fileName + '_' + str(d) + fileExt

write = 'w'



vRTR_IP = '192.168.41.11'

device = {
    'ip': '192.168.41.11',
    'username': USERNAME,
    'password': PASS,
    'device_type': 'cisco_ios'
}

#lab09 error handling
try:
    c = ConnectHandler(**device)
    output = c.send_command('show run')
    openBackup = open(backup, write)
    openBackup.write(output)
    openBackup.close()
except (AuthenticationException):
    print("An authentication error occurred while connecting to: " + device['ip'])
except(SSHException):
    print("An error occurred while connecting to device " + device['ip'] + " via ssh. Is SSH enabled?")
except(NetMikoTimeoutException):
    print("The device " + device['ip'] + " timed out when attemting to connect.")

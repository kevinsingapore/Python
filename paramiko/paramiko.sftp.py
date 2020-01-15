#!/usr/bin/python3
#-*- coding:UTF-8 -*-

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='xx.xx.xx.xx',port=22,username='username',password='password')

stdin,stdout,stderr  = ssh.exec_command("curl https://myip.ipip.net")

result = stdout.readlines()

for lines in result:
    print("info:")
    print(lines)

sftp = ssh.open_sftp()

sftp.put("/Users/kevin/py/num.txt","/data/num.txt")

stdin,stdout,stderr = ssh.exec_command("ls -al /data/")

getSure = stdout.readlines()

for Line in getSure:
    print(Line)

sftp.close()

ssh.close()

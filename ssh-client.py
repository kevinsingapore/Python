import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='xx.xx.xx.xx',port=22,username='username',password='password')

stdin,stdout,stderr  = ssh.exec_command('fdisk -l')

result = stdout.readlines()

for lines in result:
    print(lines)

ssh.close()


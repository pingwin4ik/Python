import sys
import paramiko

host = sys.argv[1]
port = int(sys.argv[2])
command = sys.argv[3]
uname = 'usr'
passwd = '1'

print host
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=port, username=uname, password=passwd)
    stdin, stdout, stderr = ssh.exec_command(command)

print stdout.read()

    ssh.close()
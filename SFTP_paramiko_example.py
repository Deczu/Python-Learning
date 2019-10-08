import paramiko
import os
from time import sleep


class Send:
    """ 
    Using Paramiko lib this module helps to exec command or send file in a simple way
    host_addr => addres of remote server
    passwd => password to remote server
    skip_rsa => if your key changes much just set it to True, should skip questions for RSA keys and replace corrupted ones

    """

    def __init__(self,host_addr,passwd,skip_rsa=False):
        self.host=host_addr
        self.passwd=passwd
        self.client=paramiko.SSHClient()
        if skip_rsa:
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def execute_command(self,command):
        stdin, stdout, srderr = self.client.exec_command(command)
        print "STD Input: " + stdin.read() + "\n"
        print "STD Output: "+ stdout.read()+ "\n"
        print "STD ERROR: " + stderr.read()+ "\n"

    def send_file(self,filename, localFPath, remoteFPath):
        transport.self.client.get_transport()
        sftp = paramiko.SFTPClient.from_transport(transport)
        if isinstance(filename,str):
            filename = [filename]
        for f in filename:
            print "Sending "+f+" from " + localFPath + " to remote path " +remoteFPath
            sftp.put(localFpath+os.sep+f, remoteFPath+os.sep+f)
            self.client.exec_command("chmod +x "+f)
    
    def __del__(self):
        print "Deleting Send object"
        self.client.close()


class Download:

    def __init__(self,host_addr,passwd,skip_rsa=False):
        self.host=host_addr
        self.passwd=passwd
        self.client=paramiko.SSHClient()
        if skip_rsa:
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def __del__(self):
        print "Deleting Download object"
        self.client.close()

    def remote_download(self, filename, remotePath, localPath):
        transport.self.client.get_transport()
        sftp = paramiko.SFTPClient.from_transport(transport)
        if isinstance(filename,str):
            filename = [filename]
        for f in filename:
            print "Downloading "
            sftp.get(remotePath+os.sep+f,localPath,os.sep+f)









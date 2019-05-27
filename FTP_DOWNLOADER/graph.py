import ftplib
import os


#check dir
def check_dir():
    path = os.getcwd()
    dirContent = os.listdir(path)
    print dirContent
    print("#"*40)
    return dirContent



dirContent = check_dir();
ftp = ftplib.FTP('ftp.sunet.se', 'anonymous', 'anonymous@sunet.se')

print "File List: "

files = ftp.dir()

lista = ftp.nlst()

print("#"*40)

ftp.cwd("/about") #changing to /pub/unix

files = ftp.dir()

print files
lista = ftp.nlst()
if 'graph.png' not in dirContent:
    print("File not in dirContent. \n Downloading new file")
    with open('graph.png', 'wb') as f:
         ftp.retrbinary('RETR ' + 'graph.png', f.write)
else:
    print("File allredy exists!")


print(type(lista))
counter = 1
for element in lista:
    print str(counter)+" " + element
    counter+=1


print("#"*40)


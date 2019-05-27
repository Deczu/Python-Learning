import ftplib

ftp = ftplib.FTP('ftp.sunet.se', 'anonymous', 'anonymous@sunet.se')

print "File List: "

files = ftp.dir()

lista = ftp.nlst()

print("#"*40)

ftp.cwd("/about") #changing to /pub/unix

files = ftp.dir()

print files
lista = ftp.nlst()
with open('graph.png', 'wb') as f:
     ftp.retrbinary('RETR ' + 'graph.png', f.write)


print(type(lista))
counter = 1
for element in lista:
    print str(counter)+" " + element
    counter+=1


print("#"*40)

counter = 1
for element in files:
    print str(counter)+" " + element
    counter+=1

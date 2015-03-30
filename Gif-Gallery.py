# -*- coding: cp1252 -*-


'''
Cria uma galeria de imagens .gif que estão na mesma pasta que o script.
-O arquivo gerado será INDEX.HTML e será aberto automáticamente
-O arquivo gerado será re-feito todas as vezes que o script for executado


This script creates a .gif gallery using the images in the same folder of the script
-The generated file will be named INDEX.HTML and will be opened automatically
-The generated file will re-made every time the script is executed


'''
import sys,os
#get the script folder
pre_files = str(sys.argv[0]).split('\\')
path= ''
for arg in pre_files[:-1]:
	path+=arg+"\\"
#get the script folder -end-

#get the files in the folder
files = os.listdir(str(path[:-1]))
print "Searching for a index.html"
#open the index.html
try:
    f = open("index.html","w")
    print "Index found."
except:
    #something went wrong
    sys.exit()
print "Writing headers."
f.write("<!DOCTYPE html>\n")
f.write("<html>\n")
f.write("<head>\n")
f.write("   <title> GIF Gallery </title>\n")
f.write("<meta charset='utf-8'>\n")
f.write("</head>\n")
print "\n\n\n\n\n\n<body>."
f.write("<body>\n")
#get all the files in the folder
#if the last 4 chars is '.gif', write the name of the gif as a <img> tag in the HTML
#else skip that file
for p in files:
    if p.endswith(".gif") == False:
        continue
    f.write("   <img src='"+str(p)+"'>\n")
print "</body>."
f.write("</body>")
print "finishing the document."
f.write("</html>")
#flush the html in the HDD
f.flush()
#closes the html
f.close()
#open your html
os.system("start " +str(path)+ "index.html") #windows only

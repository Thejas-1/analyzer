import re
import PyPDF2
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
newfile = open('hello.txt','w')
name = raw_input("Enter the file name:")
file=open(name,'rb')
pdfreader=PyPDF2.PdfFileReader(file)
print(pdfreader.getNumPages())
p = pdfreader.getNumPages()
pageobj=pdfreader.getPage(9)
input = 'random.pdf'
output = 'hello.txt'
#os.system(("ps2ascii %s %s") %( input , output))
newfile.write(pageobj.extractText())
file.close()
newfile.close()

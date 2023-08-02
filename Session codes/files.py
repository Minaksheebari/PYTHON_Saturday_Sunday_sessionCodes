def readFile():
    fileObject = open("test.csv",'r')    #You can name anything instead of fileObject.
#fileObject is a file object. like variable.

    data = fileObject.read() #read whole data
    #data = fileObject.readlines() #read multiple lines seprated by \n
    #data = fileObject.readline() #read single line
    #data = fileObject.read() # print other lines because pointer is already shifted to next line. 

#File never reads backward. 
    print(data)
    fileObject.close() #Even if program is not running, file will be closed automatically.

def writeFile():
    fileObject = open("test.csv",'a') #a will append the data in existing file.
    #x for creating new file  
    #w will clean data from existing file and add new data in that file only
    data = "\nSanjoy,24,Pune"
    fileObject.write(data)

writeFile()


import sys
def read(path,option='all'):
    try:
        file=open(path,"r")
        if file.readable():
            if isinstance(option,str):
                option.lower()
            if option=="all":
                return file.read()
            elif isinstance(option,int):
                return file.readline(option)
            elif option=="line":
                return file.readline()
            elif option=="lines":
                return file.readlines()
            file.close()
    except:
        print(sys.exc_info()[1])

def write(path,content):
    try:
        file=open(path,"w")
        if file.writable():
            if isinstance(content,str):
                return file.write(content)
            
            elif isinstance(content,list):
                return file.writelines(content)
            file.close()
    except:
        print(sys.exc_info()[1])

def append(path,content):
    try:
        file=open(path,"a")
        if file.writable():
            if isinstance(content,str):
                return file.write(content+"\n")
            
            elif isinstance(content,list):
                return file.writelines(content)
            file.close()
    except:
        print(sys.exc_info()[1])
    
    
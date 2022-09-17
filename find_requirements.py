'''
    this module will help us to find the reqired modules from a python file just like 
    pip module have one, but this will help specially for the django devlopers specially.
    (without using virtual env)
'''

def Find_req(filepath,outputfile='requirements_FDR.txt'):
    with open(filepath,"r") as pyfile:
        readedData = pyfile.readlines()
        lines_have_pacages = []
        
        
        require = []
        #checking for all lines containg form and import
        for line in readedData:
            if "import" in line :
                lines_have_pacages.append(line)

        #checking whether it is a keyword or not
        for collected_line in lines_have_pacages:
            words = collected_line.split()
            print(words)
            # if "import" in words:
            try:
                if words.index("import") == 0:
                    pk = words[1]
                    if pk not in require:
                        require.append(pk)
                    else:
                        pass 
                elif words.index("from") == 0 and words.index("import") == 2:
                    pk = words[1]
                    if pk not in require:
                        require.append(pk)
                    else:
                        pass
            except:
                pass 
        
        ofile = open(outputfile,"a+")
        for Pkg in require:
            ofile.write(f"{Pkg}\n")
        ofile.close()


Find_req("try.py")
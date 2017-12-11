import fileinput,sys,re
    
def modify_files(fileslist,patterns,backup=False):
    
    rep = dict((re.escape(k), v) for k, v in patterns.iteritems())
    pattern = re.compile("|".join(rep.keys()))
    
    if backup:
        file = fileinput.input(fileslist,inplace=1,backup=".bak")
        for line in file:
            line = pattern.sub(lambda m: rep[re.escape(m.group(0))], line)
            sys.stdout.write(line)
        file.close()

if __name__ == "__main__":
    files = ['text1.txt','text2.txt','text3.txt','text4.txt']
    patterns = {"JIRANUM": "SUMMITRM-101", "RANGENUM": "1200", "NAMEFIELD" : "PARAG RAJABHOJ"}
    modify_files(files,patterns,True)
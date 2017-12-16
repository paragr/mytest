import os,re

recursive = True
skip_list = ["error","log"]
rep = list(re.escape(k) for k in skip_list)
print rep
pattern = re.compile("|".join(rep),re.I)

for root,dirs,files in os.walk("C:\\PARAG\\PythonProgramms\\MultiProcessing\\search_files"):
    for name in files:
        fullname = os.path.join(root,name)
        match = pattern.search(fullname)
        if not match:
            print "fullfilename = %s"% fullname
    if recursive:
        pass

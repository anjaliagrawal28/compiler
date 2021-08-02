kw = ("int","float","double","main","return","printf","if","else","for","while","do","break","continue","scanf")
op = ("+","-","/","*","%","=","<",">","<=",">=","!=","==")
spsym = ("(",")","{","}",",",";","?","")
c=0
with open("c.txt","r") as f:
    with open("target.txt","w") as f1:
        for line in f:
            for k in line.split():
                if k[0] =="#":
                    f1.write(k+" is a macro\n")
                elif k in op:
                    f1.write(k+" is a operator\n")
                elif k in spsym:
                    f1.write(k+" is a special symbol\n")
                elif k in kw:
                    f1.write(k+" is a keyword\n")
                elif k.isdigit():
                    f1.write(k+" is a integer\n")
                elif "%" in k:
                    f1.write(k+" is a format specifer\n")
                elif k.isalnum() and k[0].isalpha():
                    f1.write(k+" is a Variable\n")
                else:
                    f1.write("Lexical error encountered\n")
            c = c+1
        f1.write("Total number of lines in code "+str(c))

     
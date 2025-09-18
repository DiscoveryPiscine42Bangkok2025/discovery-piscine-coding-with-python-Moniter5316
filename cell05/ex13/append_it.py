import sys 
if len(sys.argv) > 1 :
    text = sys.argv[1:]
    for i in text :
        if i.endswith("ism") :
            print(end="")
        else :
            print(i+"ism")                   
else :
    print("none")
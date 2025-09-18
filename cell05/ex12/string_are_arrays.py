import sys
text = sys.argv[1:]

if len(text) == 1 :
    
    cont = text.count("z")

    if cont == 0 :
        print(text)
    else :
        print("z"*cont)
else :
    print("none")   
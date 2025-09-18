import sys
text = sys.argv[1]
if len(sys.argv[1:]) == 1 :
    
    cont = text.count("z")

    if cont == 0 :
        print("none")
    else :
        print("z"*cont)
else :
    print("none")
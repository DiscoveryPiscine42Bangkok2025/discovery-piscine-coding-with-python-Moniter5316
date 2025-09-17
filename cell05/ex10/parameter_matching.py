import sys 
keyword = sys.argv[1]
if len(sys.argv) !=2 :
    print("none")
else:
    mes = input("What was the parameter? ")
    if mes == keyword :
        print("Good job!")
    else:
        print("Nope, sorry...")
import sys
mes = sys.argv[1:]
if len(mes) != 2 :
    print("none")
else :
    keyword = mes[0]
    text = mes[1]
    cont = text.count(keyword)

    if cont == 0 :
        print("none")
    else :
        print(cont)
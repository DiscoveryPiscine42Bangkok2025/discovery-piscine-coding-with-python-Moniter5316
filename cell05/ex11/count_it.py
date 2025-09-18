import sys
mes = sys.argv[1:]
if len(sys.argv) >2 :
    print("parameters:",len(sys.argv)-1)
    for i in mes :
        print(f"{i}: {len(i)}")
else :
    print("none")
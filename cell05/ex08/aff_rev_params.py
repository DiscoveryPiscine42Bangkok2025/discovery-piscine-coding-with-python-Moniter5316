import sys

params = sys.argv[1:]
if len(params) >=2 :
    for i in reversed(params) :
        print(i)
else :
    print("none")

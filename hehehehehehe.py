winnum = {10, 11, 8, 1, 5, 20}
uname, *unumstr = input().split()

if len(unumstr) != 6:
    print("Should be 6 numbers")
    quit()

unum = set()
for numstr in unumstr:
    num = int(numstr)
    if num in unum:
        print("No Duplicates.")
        quit()
    unum.add(num)

nummatched = len(winnum & unum)
prizemoney = nummatched * 100

if nummatched > 0:
    print(f"{uname} won {prizemoney} pesos!")
else:
    print(f"{uname} won nothing!")

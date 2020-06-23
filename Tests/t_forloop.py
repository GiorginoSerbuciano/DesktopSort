for x in range(3,5):
    print("We came %d"%(x),"th!")

scan = obj
for item in scan:
    if item.is_dir() or item.is_file():
        print(item.name)


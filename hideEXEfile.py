imgLoc = input("Image location >>> ")
exeLoc = input("EXE location >>> ")
with open(imgLoc, 'ab') as f, open(exeLoc, "rb") as e:
    f.write(e.read())

print("Done!")
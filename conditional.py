
speed = int(input("what was your average speed?"))
allowed_speed = int(input("what was your allowed speed"))
if speed > allowed_speed:
    demerit =(speed - allowed_speed )//5
    print (demerit)
    if demerit>=12:
        print("Time to go to jail")
elif speed<=allowed_speed:
    print("Ok")
else:
    print("incorrect entry")

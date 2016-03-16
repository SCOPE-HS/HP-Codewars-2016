mybool = True
while mybool == True:
    myinput = input()
    a,b = myinput.split(" ")
    if(myinput == "0 0"):
        mybool = False
    multiplynum = pow(10.0, float(b))
    if(myinput != "0 0"):
        output = round(float(a)*float(multiplynum), 2)
        splo = str(output).split('.')
        if splo[-1] == '0':
            splo[-1] = '00'
        print('.'.join(splo))

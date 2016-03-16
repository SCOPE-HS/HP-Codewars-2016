numLines = int(input())
import math
for i in range(numLines):
    line = input().split()
    if ("+" in line[5]):
        line[5] = line[5][1:]
    name = line[0]
    #print("name = " + name)
    #line = str(line).split()
    RAh = float(line[1])
    #print("RAh = " + str(RAh))
    RAm = float(line[2])
    #print("RAm = " + str(RAm))
    decd = float(line[3])
    #print("decd = " + str(decd))
    decm = float(line[4])
    #print("decm = " + str(decm))
    LY = float(line[7])
    #print("LY = " + str(LY))
    RA = 15.0*RAh + 0.25*RAm
    dec = decd + (decm / 60.0)
    r = LY
    theta = (90.0-dec) * 3.14 / 180.0
    phi = RA * math.pi/180.0
    #print(str(math.sin(theta)))
    #print(str(math.cos(phi)))
    x = r*math.sin(theta)*math.cos(phi)
    y = r*math.sin(theta)*math.sin(phi)
    z = r*math.cos(theta)
    x = round(x, 2)
    y = round(y, 2)
    z = round(z, 2)
    print(name + " x=" + str(x) + ", y=" + str(y) + ", z=" + str(z))

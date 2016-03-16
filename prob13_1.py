numLines = int(input())
import math
for i in range(numLines):
    line = input().split()
    if ("+" in line[5]):
        line[5] = line[5][1:]
    name = line[0]
    #line = str(line).split()
    print(line[1])
    print(line[3])
    RAh = float(line[1])
    RAm = float(line[2])
    decd = float(line[3])
    decm = float(line[4])
    LY = float(line[7])
    RA = 15.0*RAh + 0.25*RAm
    dec = decd + (decm / 60.0)
    r = LY
    theta = (90.0-dec) * math.pi / 180.0
    phi = RA * math.pi/180.0
    x = r*math.sin(theta)*math.cos(phi)
    y = r*math.sin(theta)*math.sin(phi)
    z = r*math.cos(theta)
    print(name + " x=" + str(x) + ", y=" + str(y) + ", z=" + str(z))
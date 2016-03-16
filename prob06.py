numInputs = input()
for i in range(int(numInputs)):
    line = input()
    mList = line.split(" ")
    T = int(mList[0])
    T0 = int(mList[1])
    T1 = int(mList[2])
    C0 = int(mList[3])
    C1 = int(mList[4])
    Solution = (T / (((T1/C1)+(T0/C0))/2))/8
    print(round(float(Solution)))
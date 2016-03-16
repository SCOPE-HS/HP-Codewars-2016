shifts = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':1,'G':2,'H':3,'I':4,'J':5,'K':1,'L':2,'M':3,'N':4,'O':5,'P':1,'Q':2,'R':3,'S':4,'T':5,'U':1,'V':2,'W':3,'X':4,'Y':5,'Z':1,' ':6}
numInputs = input()
for i in range(int(numInputs)):
    S = input()
    ind = 0
    final = ""
    while len(S) > 0:
        #if (ind >= len(S)):
        #    ind -= len(S)
        print(len(S))
        final += S[ind%len(S)]
        oldI = S[ind%len(S)]
        Slist = list(S)
        Slist.pop(ind%len(S))
        S = ''.join(Slist)
        ind += shifts[oldI] - 1
        print(final)

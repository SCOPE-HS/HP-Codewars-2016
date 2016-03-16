alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
doubles = [char * 2 for char in alphabet]



myinput = int(input())
while(myinput != 0):
    myinput = myinput - 1
    someinput = input()
    if any([d in someinput for d in doubles]):
        print('likes {}'.format(someinput))
    else:
        print('hates {}'.format(someinput))
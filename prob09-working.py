while True:
    line = input()
    if line != "0 0 0":
        mValues = line.split(" ")
        length = int(mValues[0])
        width = int(mValues[1])
        height = int(mValues[2])
        volume = length*width*height
        answer = (volume - ((2*length*height)+(2*width*height)+(2*width*length)-(4*height)-(4*width) - (4*(length - 2))))
        print(answer)
        print(volume)
        if (answer < (volume / 2)):
            print("A "+str(length)+"x"+str(width)+"x"+str(height)+" block is MORE than Perfect.")
        elif (answer > (volume / 2)):
            print("A "+str(length)+"x"+str(width)+"x"+str(height)+" block is LESS than Perfect.")
        else:
            print("A "+str(length)+"x"+str(width)+"x"+str(height)+" block is PERFECT.")
    else:
        break
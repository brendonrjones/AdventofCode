## Creates list
with open('block.csv', 'r') as array:
    numbers = list()
    numbers = [int(val) for val in array]
## Initialises values
f = len(numbers)
s=0
high_ind=0
check = False
track=[]
track.append(list(numbers))
count=0
print("numbers: ",numbers,"length: ",len(numbers))
print("track: ",track,"length: ",len(track))
print("Step Count: ",count)
while True:
##Loop to find highest integer.
    for num in range(s,f):
        if numbers[num]>numbers[high_ind]:
            high_ind=num
    hand=numbers[high_ind]
    numbers[high_ind]=0
    curr_ind=high_ind+1
## Loop to distribute highest value
    while hand > 0:
        if curr_ind <= (f-1):
            calc=numbers[curr_ind]
            numbers[curr_ind] = calc + 1
            curr_ind += 1
            hand -= 1
        else:
            curr_ind = 0
    count += 1
    track.append(list(numbers))
## Check to see if there are any copies.
    row_count=0
    if count > 0:
        for row in track[0:(len(track)-1)]:
            col=0
            if check == True:
                break
            for val in row:
                if check == True:
                    break
                if val==track[count][col]:
                        col+=1
                if col==len(row):
                    print("YAHOO")
                    print(row,track[count])
                    print("FINAL Step Count: ",count)
                    print("It took ",count-row_count,"to find a repeating set of values")
                    check=True
                    break
            row_count+=1
    if check == True:
        break

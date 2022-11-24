name = input("Enter name: ")#getting user input and also creating variable name
arr = []#creating an array for storing multiple numbers

for x in range(5): #for loop using range() function
    arr.append(int(input("Enter number: ")))#adding user input numbers to the array per iteration

sum =0  #declaring a variable sum and initializing to 0

for i in range(5):
    sum += arr[i]  #adding contents of the array

print(sum)#printing out the value of sum

average = sum / 5#calculating the average

print(name + ", you have entered the numbers: " + str(arr[0]) + ", " + str(arr[1]) + ", " +
      str(arr[2]) + ", " + str(arr[3]) + ", "+ str(arr[4]))#printing out all the numbers from the user

print("The sum is: " + str(sum))#printing out the sum
print("The average is: " + str(average))#printing out the average
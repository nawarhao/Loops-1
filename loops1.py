#input an integer value
n = int(input("Enter the number whose sum you want to find: "))
sum = 0

#Iterates for n+1 times: i=1 to n+1
for i in range(1, n+1):
    sum = sum+i
    print("\nSum =", sum)
    
#Input a word or sentence
string = input("Please enter your own string: ")

string2 = ('')
#loop for printing in reverse
for i in string:
    string2 = i+string2
    
print("\nThe Original String =", string)
print("The Reversed String =", string2)

# Input number greater than 1
n = int(input("Enter the value of n: "))

# print the numbers from n to 1
print("numbers from {0} to {1} are:" .format(n,1))

# loop to print numbers
for i in range(n,0,-1):
    print(i)
    
#Take input of a string
str1 = input("PLease Enter a sentence: ")
total = 1 #initialise 

print(len(str1))
for i in range(len(str1)):
#loop will run to calculate the length using string operation
    if(str1[i] == ' '): #Finding number of words in a sentence by checking the spaces
    #condition 1 
        total = total + 1
        
print("Total number of words in this string = ", total)

#Finding sum of even numbers in a range
s1 = 0
for i in range(10, 21):
    if i %2 == 0:
        s1 = s1+i
        
print("Sum of even numbers between 10 and 20 is", s1)
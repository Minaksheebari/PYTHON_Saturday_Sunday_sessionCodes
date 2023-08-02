#list from where I will display the values of the list

students = ["Sohail","Minakshee","Urvashi","Vaibhav"]
print(students)     #direct printing

print(students[0])  #print using index
print(students[1])
print(students[2])
print(students[3])

for names in students:  #print using loop
    print(names)

#printing charecters in string
word = "HeroVired" #word = input("Enter string: ")

#using while loop
i=0
while i< len(word):
    print(word[i])

    i+=1

#using for loop 
for letter in word:
    print(letter)

#printing tables
num1=int(input("Enter the number: "))
i=1

#using while loop
while i<=10:
    result= num1 * i
    print(num1, "*", i, "= ",result)
    i+=1
   
#using for loop
for i in range(1,11,1):
    product=num1 * i
    print(product)

#printing stars * in / 2nd line ** / in 3rd line ***
symbol = "*"
i = 1
for i in range(1,11,1):
    new = symbol * i
    print(new)

#another method
# i = 0
# j = 0

# for i in range(5):
#     for j in range(i):
#         i = i + j
#         print("*", end="")
#     print()

#print count of number of digits in given number
num2 = int(input("Enter any number: "))
count = 0
while num2!=0:
    num2 = num2 // 10 
    print("New value of num: ",num2)  #to show new value of number
    count += 1
    print("New count: ", count)
print("count = ",count)

#printing common letters in string
def common_letters(string_one,string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common
print(common_letters("banana", "sabuna"))



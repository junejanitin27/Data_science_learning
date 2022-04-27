#if-else practice
x = 2
if(x<5):
    print(x)


if(x>1 and x <5):
    print(x)

#Score code
score = 40

if (score>=75):
    print("You passed!")
elif(score >= 50 and score<75):
    print("Try again")
else:
    print("Please see your teacher")


#Even or #odd code

x = int(input("Enter a number: "))

if (x%2==0):
    print("Number if Even")
else:
    print("Number is odd")

# Student Grades (Part 2)

grades = [77, 99, 48, 80, 67]
total = len(grades)
print(total)
pass_number = 0
for i in grades:
    if(i>=75):
        pass_number = pass_number + 1

print(pass_number)
pass_rate =  (pass_number/total)*100
print("Pass_rate is ", pass_rate)


#Infinite loop Example

#answer = input("Run again? (Y/N) ").lower()

#while(answer):
  #if answer =='n':
    #break
  #print("continue")


#Define a function that returns true if one student passes, and false if they fail.
def helper(grade):
  if(grade>=75):
    return True
  else:
    return False



#Define a function that uses helper to find the pass rate of a class.
def pass_rate(grades):
  total_passed = 0
  for i in grades:
    pass_1 = helper(i)
    if(pass_1 == True):
      total_passed += 1
  return total_passed/len(grades) * 100

#Given a list of grades, use the function you just made to find the pass rate.
grades = [77, 99, 48, 80, 67]
pass_rate(grades)
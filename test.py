#Example for Infinite_loop


answer = input("Run again? (Y/N) ").lower()

while(answer):
  if answer =='n':
      break
  elif answer == 'y':
      print("continue")
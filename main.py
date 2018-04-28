#Wk14_TeamGitHubProgram - Average Test Score
#This program will prompt the user for the total number of tests they have taken, their test scores for each tests, and then calculate the average of the test scores. The average of the test scores will then be outputted along with the appropriate letter grade.
#Ben, Dan, Kyle, Lisa, and Lia all worked on this program together during class.
#April 28, 2018

#Declaring variables
totalTests = 0.0
testAverage = 0.0

#Welcoming the user
print("Welcome to the Average Test Score program!")

print()

#Inputting the user's number of tests they've taken
while True:
  try:
    numberOfTests = int(input('How many tests have you taken?'))
    if (numberOfTests <= 0):
      print()
      print("*** ERROR: Must enter at least 1 ***")
      print()
    else:
      break
  except ValueError:
    print()
    print("*** ERROR: Not an integer ***")
    print()

print()

#Using a for loop to input the user's test scores and then add them together
for x in range(0, numberOfTests):
    print(("Test Number %d") % (x + 1))
    
    while True:
      try:
        testScore = float(input("Enter your test score:"))
        if (testScore < 0):
          print()
          print("*** ERROR: Test score cannot be lower than 0 ***")
          print()
        elif (testScore > 100):
          print()
          print("*** ERROR: Test score cannot be higher than 100 ***")
          print()
        else:
          break
      except ValueError:
        print()
        print("*** ERROR: Not a number format ***")
        print()
    
    print()
    totalTests = totalTests + testScore

#Calculating average
testAverage = (totalTests / numberOfTests)

#Outputs & formats the average to have 2 decimal places
print(("Average Test Score:"), (format(testAverage, '.2f')), ("%"))

print()

#if...elif...else statements to find and output the correct letter grade for the average test score 
if (testAverage >= 90):
  print("You've received an A for your letter grade!")
elif (testAverage >= 80 and testAverage <=89):
  print("You've received a B for your letter grade!")
elif (testAverage >= 70 and testAverage <=79):
  print("You've received a C for your letter grade!")
elif (testAverage >= 60 and testAverage <=69):
  print("You've received a D for your letter grade!")
else: 
  print("You've received a F for your letter grade!")
  
print()

#Informing the user that the program has ended
print("Thank you for using the Average Test Score program!")

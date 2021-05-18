print("Welcome to the Sorting Hat! I, the sorting hat, will ask you a few questions that you need to answer truthfully to be put into your house.")
points = 0

def answer() : 
  choice = input()
  if choice == "I":
    points += 1
  elif choice == "II":
    points += 2
  elif choice == "III":
    points += 3
  elif choice == "IV":
    points += 4

print("Enter your answers in this format: 'I', 'II', 'III', 'IV'")

print("Question 1: World War III has broken out and you have joined your countries military? What do you do?")
print("I: Charge into battle!")
print("II: Be extremely helpful to all your fellow soldiers.")
print("III: Share an excellent battle plan with your general that may lead your side to victory.")
print("IV: Be extremely helpful to your general in hope of ranking up.")

answer()



print("Question 2: You have gained the position of general, and conquer an enemy town with a population of 5 million. What do you do?")
print("I: Let it be.")
print("II: Help rebuild it.")
print("III: Let it be, but keep some troops to guard it.")
print("IV: Burn it to the ground.")

answer()





print("Question 3: You are approaching the enemy city, what do you do?")
print("I: Charge into it.")
print("II: Wait for renforcements.")
print("III: Surround it and then wait for renforcements.")
print("IV: Surround it, slowly advance, and take it over. If they show signs of resistance burn it to the ground.")

answer()





print("Question 4: You have won the war and recieve 50 billion dollars. How do you spend it?")
print("I: Keep all of it.")
print("II: Spend all of it on rebuilding.")
print("III: Keep 25 billion and spend 25 billion on rebuilding.")
print("IV: Spend as much as is needed on rebuilding and keep the rest.")
answer()

  
  
  
  
  
#If you have a suggestion for a new question, do it in this format:
#print("Question questionnumber: The question?")
#print("I: Choice 1.")
#print("II: Choice 2.")
#print("III: Choice 3.")
#print("IV: Choice 4.")
#choice3 = input()
#if choice3 == "I":
#  points += 1
#elif choice3 == "II":
#  points += 2
#elif choice3 == "III":
#  points += 3
#elif choice3 == "IV":
#  points += 4




if points < 7:
  print("You are in Gryffindor! You are extremely brave but sometimes don't think before you act, getting you into incredibly stupid situations.")
elif points < 10:
  print("You are in Hufflepuff! You are extremely hard-working and loyal, but can be manipulated easily.")
elif points < 13:
  print("You are in Ravenclaw! You are extremely smart, but can be too full of yourself sometimes.")
elif points <= 16:
  print("You are in Slytherin! You are extremely ambitious, but can sometimes take things too far.")

from constants import YES, CENTRAL_PROCESSING_UNIT, POWER_SUPPY_UNIT, GRAPHICS_PROCESSING_UNIT

print("Welcome to my computer quiz")
initiate = input("Do you wanna play the Quiz game? ").lower()
if initiate != YES:
    quit()
print("Okay! Let's play!!!")
score = 0
answer = input("What does CPU stand for? ").lower()
if answer == CENTRAL_PROCESSING_UNIT:
    print('Correct✅')
    score += 1
else:
    print('Incorrect❌')

answer = input("What is PSU? ").lower()
if answer == POWER_SUPPY_UNIT:
    print('Correct✅')
    score += 1
else:
    print('Incorrect❌')

answer = input("What does GPU stand for? ").lower()
if answer == GRAPHICS_PROCESSING_UNIT:
    print('Correct✅')
    score += 1
else:
    print('Incorrect❌')

print(f"Your final score is {score}")
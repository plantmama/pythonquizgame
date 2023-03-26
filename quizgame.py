# QUIZ GAME START UP

# THIS GAME IS A BOT ASKING BASIC QUESTIONS WITH ONE WORDED ANSWERS
print("THIS GAME IS A BOT ASKING FOUR BASIC QUESTIONS WITH ONE WORDED ANSWERS...")
# WE HAVE FOUR QUESTIONS
# LET'S SEE IF THE USER WANTS TO PLAY
playerInput = input("DO YOU WISH TO SEEK YOUR FORTUNE...  ")

if playerInput.lower() != "yes":
    quit()


print("Alllrrrriiiight then :/")
score = 0
# QUESTION ONE: "WHAT COLOR WERE THE FIRSTS TESLAS"  (WHITE)
playerAnswer = input("WHAT COLOR WERE THE FIRST TESLAS?  ")
if playerAnswer.lower() == "white":
    print("omg, who are you! Great Job!")
    score += 25
else:
    print("Not even close, but still great effort <3")

# QUESTION TWO: "WHAT YEAR WAS WW2"   (1939)
playerAnswer = input("WHAT YEAR WAS WW2?  ")
if playerAnswer.lower() == "1939":
    print( "Woohooo! Nice one")
    score += 25
else:
    print("NOPE")
# QUESTION THREE: "WHAT WAS OUR FIRST PRESIDENTS LAST NAME"    (WASHINGTON)
playerAnswer = input("WHAT WAS OUR FIRST PRESIDENTS LAST NAME?  ")
if playerAnswer.lower() == "washington":
    print("You so smart, you history buff, you")
    score += 25
else:
    print("Think again")
# QUESTION FOUR: "WHAT YEAR WAS THE GREAT DEPRESSION START"   (1929)
playerAnswer = input("WHAT YEAR DID THE GREAT DEPRESSION START?  ")
if playerAnswer.lower() == "1929":
    print("Lets GoOoOoOoOoOOoOo")
    score += 25
else:
    print("NOPE")
# NOW LET'S COUNT OUR SOLUTIONS
# NPC CORRECT OPTIONS:
# "Woohooo! Nice one"
# "omg, who are you! Great Job!"
# "Lets GoOoOoOoOoOOoOo"
# "You so smart, you history buff, you"

# NPC INCORRECT OPTIONS:
# "WRONG, try again though, you got this"
# "Not even close, but still great effort <3"
# "Nope."
# "Think again"

# END OF QUIZ REACTION: "GOOD JOB, YOU ARE FINISHED"
print("GOOD JOB, YOU ARE FINISHED, YOU SCORED  " + str(score))

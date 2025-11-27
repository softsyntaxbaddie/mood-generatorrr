
import random
name = input("What is your name?").upper()

happy_messages =[
    "YOU GOT THIS!",
    "SLAY TODAY!",
    "TODAY IS YOUR DAY!",
    "HYPE MODE ACTIVATED!"
]

sad_messages =[
    "YOU ARE STRONGER THAN YOU THINK!",
    "KEEP PUSHING BESTIE!",
    "THIS TOO SHALL PASS!",
    "TOMORROW THE SUN WILL RISE AGAIN AND SO WILL YOU!"
]

stressed_messages =[
    "TAKE A DEEP BREATH!",
    "FOCUS AND CONQUER!",
     "ONE STEP AT A TIME!",

]
print("\nType 'quit' anytime to stop the hype!\n")

while True:
    mood =input("How are you today? (happy,sad,stressed):").lower()

    if mood == "quit":
        print(f"{name}, SEE YOU NEXT TIME! BYE- BYE!")
        break

    if mood =="happy":
        print(f"{name},{random.choice(happy_messages)}")
    elif mood == "sad":
         print(f"{name},{random.choice(sad_messages)}")
    elif mood == "stressed":
        print(f"{name},{random.choice(stressed_messages)}")
    else:
        print(f"{name},I DONT KNOW THAT VIBE BUT KNOW THAT YOU ARE UNSTOPPABLE TODAY!")

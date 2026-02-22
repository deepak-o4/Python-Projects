import random
# create subjects 
subjects = [
    "Salman Khan",
    "Dhoni", 
    "Narendra Modi",
     "Bill Gates",
     "Justin Bieber",
     "Deepak",
     "Trishika",
]
# create actions
actions = [
    " launches",
    "eats",
    " travels to",
    "orders",
    "pays for",
    "loves",
    "wants to masrry"
]

# create plsces or things 

places_or_things = [
    "at red fort",
    "Delhi metro",
    "eats dosa",
    "in kashi at ganga ghat",
    " to annoy Deepak"
]
# start the headline genration loop

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} {action} {places_or_thing} "
    print("\n" + headline)

    user_input = input("\nDo you want to generate another headline? (yes/No)").strip().lower() #strip removes extra spaces from thr user input and lower coverts it into lowercase 
    if user_input == "no":
        break

    #print a goodbye message
print("\nThanks for using the Fake news Headline generator.")
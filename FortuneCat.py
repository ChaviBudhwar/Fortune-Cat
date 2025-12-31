import random
fortunes = [
    "A fresh start is coming your way!", "Your kindness will be rewarded soon.",
    "A thrilling adventure is in your future.", "Someone is thinking fondly of you right now.",
    "Your hard work is about to pay off.", "A beautiful surprise is waiting around the corner.",
    "Expect a phone call that makes you smile.", "You will find something you thought you lost.",
    "A small act of kindness will bring you great joy.", "Your creativity will lead to success.",
    "Good news is headed to your mailbox.", "You are more capable than you realize.",
    "A new friendship is blooming.", "Your positive energy is contagious!",
    "Today is a great day to start something new.", "An old friend will reach out soon.",
    "A dream you have will soon come true.", "You will find inspiration in the simplest things.",
    "A peaceful mind brings a happy life.", "Your smile is your best asset.",
    "Success is in your near future.", "You will discover a new talent.",
    "A fun trip is being planned for you.", "Your heart will be filled with gratitude today.",
    "You are exactly where you need to be.", "Great things take time, stay patient!",
    "A happy coincidence will brighten your week.", "You will make someone's day today.",
    "Your intuition is leading you the right way.", "A moment of clarity is coming.",
    "Laughter will fill your home tonight.", "You are loved more than you know.",
    "A career breakthrough is on the horizon.", "Your bravery will open new doors.",
    "A simple joy will make you very happy.", "You will overcome a challenge with ease.",
    "A golden opportunity is about to present itself.", "Your generosity will return to you tenfold.",
    "Keep going, you're doing amazing!", "A pleasant surprise is in your pocket.",
    "You will find beauty in the ordinary.", "Your passion will lead you to greatness.",
    "A new door is opening for you.", "Your future is bright and full of hope.",
    "You will receive a compliment that stays with you.", "A cozy evening is in your future.",
    "Your determination will get you far.", "A lucky star is watching over you.",
    "You will find peace in a busy day.", "Your ideas are worth sharing.",
    "A burst of energy will help you finish your goals.", "You will be surrounded by good vibes.",
    "A kind word will change your perspective.", "Your patience is about to be rewarded.",
    "A new hobby will bring you much joy.", "You will find a reason to celebrate soon.",
    "Your confidence is growing every day.", "A mystery will be solved in your favor.",
    "You are making a difference in the world.", "A relaxing weekend is ahead.",
    "Your strength is inspiring to others.", "A thoughtful gift is coming your way.",
    "You will find a shortcut to your goals.", "Your focus will lead to a big win.",
    "A new perspective will bring you peace.", "You will attract positive people today.",
    "Your wisdom is beyond your years.", "A delicious meal is in your future.",
    "You will find balance in your life.", "Your curiosity will lead to a great discovery.",
    "A sunny day is coming to match your mood.", "You will be the reason someone smiles today.",
    "Your potential is limitless.", "A happy memory is about to be made.",
    "You will find the answer you’ve been looking for.", "Your loyalty is a rare and beautiful thing.",
    "A celebration is in order!", "You will master a skill you've been practicing.",
    "A feeling of accomplishment is coming.", "Your workspace will become a place of joy.",
    "You will find comfort in a familiar place.", "A new chapter is starting, and it’s a good one.",
    "Your light shines bright for all to see.", "A helping hand will appear when you need it.",
    "You will find a new favorite song today.", "Your honesty will bring you respect.",
    "A group project will go perfectly.", "You will feel a deep sense of contentment.",
    "Your presence is a gift to those around you.", "A short walk will bring a big idea.",
    "You will find a hidden treasure (even if it's small!).", "Your resilience is your superpower.",
    "A new opportunity for growth is coming.", "You will feel refreshed and renewed soon.",
    "Your kindness is a ripple in a pond.", "A spark of joy will ignite your day.",
    "You will find harmony in your relationships.", "Your best days are still ahead of you.",
    "A fluffy kitten (or puppy) thought is sent your way!"
]
pickedF = random.choice(fortunes)

cat = """
                       /)
              /\___/\ ((
              \`@_@'/  ))
              {_:Y:.}_//
--------------{_}^-'{_}--------------
"""
print (cat)
response = input ( """Would you like to know your fortune?  

-------------------------------------
       """).lower().strip()

if response == "yes":
    print (cat + pickedF)
    print ("---------------------------------------")
else:
    print (cat + "Thanks for visiting!")
    print ("-------------------------------------")
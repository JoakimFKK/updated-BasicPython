import random

# Dictionary = key: value
capitals = {
    'Alabama': 'Montgomery',
    'Alaska': 'Juneau',
    'Arizona': 'Phoenix',
    'Arkansas': 'Little Rock',
    'California': 'Sacramento',
    'Colorado': 'Denver',
    'Connecticut': 'Hartford',
    'Delaware': 'Dover',
    'Florida': 'Tallahassee',
    'Georgia': 'Atlanta',
}

# Get random value from a list of 'capitals.keys()'
random_state = random.choice(list(capitals.keys()))

while True:
    user_input = input(f"What is the capital of {random_state}?")
    if user_input.lower() == capitals[random_state].lower():
        print("correct")
        break
    elif user_input.lower() == "exit":
        break
    else:
        print("false")
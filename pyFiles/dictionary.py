def initial_intro():
    quotes = {
        "Salinger" : "I thought what I'd do was, I'd pretend to be one of those deaf-mutes",
        "Caesar" : "Veni Vidi vici",
        "Insane Person" : "Shakespeare was actually a collective of people, and not actually a person"
    }
    ## Adding more to the dictionary;
    # 4: "People always ask me when there's going to be another one"
    quotes[4] = "People always ask me when there's going to be another one"
    # 'art': "Egads! My roast is ruined"
    quotes["art"] = "Egads! My roast is ruined"

    print(quotes["Salinger"]) # output: "I thought what I'd do was, I'd pretend to be one of those deaf-mutes"
    print(quotes["Caesar"]) # output: Veni Vidi vici
    print(quotes["Insane Person"]) # output: Shakespeare was actually a collective of people, and not actually a person
    print(quotes[4]) # output:  People always ask me when there's going to be another one

    foobar = "Salinger"

    if foobar in quotes:
        print(quotes[foobar]) # output: "I thought what I'd do was, I'd pretend to be one of those deaf-mutes"

    for key, value in quotes.items():
        print(f"{key} wrote; '{value}'")
        """OUTPUT:
            "Salinger" : "I thought what I'd do was, I'd pretend to be one of those deaf-mutes",
            "Caesar" : "Veni Vidi vici",
            "Insane Person" : "Shakespeare was actually a collective of people, and not actually a person"
            4 : "People always ask me when there's going to be another one"
            "art" : "Egads! My roast is ruined"
        """

def person_data():
    person_data["name"] = input("What is your name? ")
    person_data["age"] = int(input("What is your age? "))
    person_data["nationality"] = input("What is your nationality? ")
    # person_data = { 'name': '[INPUT]', 'age': '[INPUT]', 'nationality': '[INPUT]'}


def review_exercises():
    captains = {} # empty dictionary
    captains["Enterprise"] = "Picard"
    captains["Voyager"] = "Janeway"
    captains["Defiant"] = "Sisko"

    if not "Enterprise" in captains: # if "Enterprise" isn't in captains
        captains["Enterprise"] = "unknown"  # add Enterprise with the value "unknown"
    if not "Discovery" in captains:
        captains["Discovery"] = "unknown"

    for ship, captain in captains.items():
        print(f"The {ship} is captained by {captain}.")
    print("\n\n")
    del captains["Enterprise"] # deletes Enterprise
    for ship, captain in captains.items():
        print(f"The {ship} is captained by {captain}.")
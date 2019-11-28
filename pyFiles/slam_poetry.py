# https://i.kym-cdn.com/entries/icons/original/000/020/546/7e7.jpg
import random

def make_poem(n1, n2, n3, v1, v2, v3, a1, a2, a3, p1, p2, a):
    return print(f"A {a1} {n1}\n\nA {a1} {n1} {v1} {p1} the {a2} {n2} {a1}, the {n1} {v2}\nthe {n2} {v3} {p2} a {a3} {n3}")


## Lists
# The lists are created by splitting the strings by the comma, turning them into an IEnumerable
nouns = "fossil, horse, aardvark, judge, chef, mango, extrovert, gorilla".split(", ")
verbs = "kicks, jingles, bounces, slurps, meows, explodes, curdles".split(", ")
adjectives = "furry, balding, incredolous, fragrant, exuberant, glistening".split(", ")
prepositions = "against, after, into, beneath, upon, for, in, like, over, within".split(", ")
adverbs = "curiously, extravagantly, tantalizingly, furiously, sensuously".split(", ")

## Strings
# To ensure that the loops will run at least once.
noun1, noun2, noun3 = "", "", ""
verb1, verb2, verb3 = "", "", ""
adjective1, adjective2, adjective3 = "", "", ""
preposition1, preposition2 = "", ""
adverb = random.choice(adverbs)

## Getting random words
# While some of the words are the same, get random values.
while noun1 == noun2 or noun1 == noun3 or noun2 == noun3:
    noun1 = random.choice(nouns)
    noun2 = random.choice(nouns)
    noun3 = random.choice(nouns)
while verb1 == verb2 or verb1 == verb3 or verb2 == verb3:
    verb1 = random.choice(verbs)
    verb2 = random.choice(verbs)
    verb3 = random.choice(verbs)
while adjective1 == adjective2 or adjective1 == adjective3 or adjective2 == adjective3:
    adjective1 = random.choice(adjectives)
    adjective2 = random.choice(adjectives)
    adjective3 = random.choice(adjectives)
while preposition1 == preposition2:
    preposition1 = random.choice(prepositions)
    preposition2 = random.choice(prepositions)

# print it out as a poem.
make_poem(noun1, noun2, noun3, verb1, verb2, verb3, adjective1, adjective2, adjective3, preposition1, preposition2, adverb)
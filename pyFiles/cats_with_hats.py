"""You have 100 cats.
    One day you decide to arange all your cats in a giant circle.
    Initially, none of your cats have any hats on.
    You walk around the circle 100 times, always starting at the same spot, with the first cat.
    Every time you stop at a cat, you either put a hat on it if it doesn't have one,
    or you take its hat off if it has one on.

    1. The first round you stop at every cat.
    2. The second round you only stop at every other cat(#2, #4, #6, etc.)
    3. The third round you only stop at every other cat(#3, #6, #9, etc.)
    4. You continue this process until you've made 100 rounds around the cats.
"""

def get_cats_with_hats():
    # Der bliver oprettet 100 + 1 katte, altså 0-101, hvor 0 bliver ignoreret.
    cats = [False] * (100 + 1)
    hatgiver = 0
    # Vi starter på 1, altså ignorer den nulte, ikke eksisterende kat.
    for i in range(1, 100 + 1):
        hatgiver = i
        while hatgiver <= 100:
            # Cat has hat, removes hat
            if cats[hatgiver] is True:
                cats[hatgiver] = False
            # cat no hat, give hat
            else:
                cats[hatgiver] = True
            hatgiver += i
    cats_with_hats = []
    for cat_number in range(1, 100 + 1):
        if cats[cat_number] is True:
            cats_with_hats.append(cat_number)
    return cats_with_hats

print(get_cats_with_hats())
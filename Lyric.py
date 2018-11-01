def add_lyrics(frequency, song):
    word = ""
    for i in song:
        word += i
        if i == " ":
            try:
                frequency[word] += 1
            except KeyError:
                frequency[word] = 1
            word = ""
    return frequency


def user_menu():
    pass


frequency = {}
song = "Cold! The air and water flowing. Hard! The land we call our home. Push! To keep the dark from coming. Feel! " \
       "The weight of what we owe. This! The song of sons and daughters. Hide! The heart of who we are. Making peace " \
       "to build a future. Strong united working 'til we fall. Cold! The air and water flowing. Hard! The land we " \
       "call our home. Push! To keep the dark from coming. Feel! The weight of what we owe. This! The song of sons " \
       "and daughters. Hide! The heart of who we are. Making peace to build a future. Strong united working 'til we " \
       "fall. And we all lift, and we're all adrift, Together, together. Through the cold mist, 'til we're lifeless" \
       "Together, together" # We All Lift Together - Keith Power
song = song.lower()
frequency = add_lyrics(frequency, song)
print(frequency)


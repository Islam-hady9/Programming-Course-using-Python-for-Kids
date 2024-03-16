def mad_libs():
    story = "Once upon a time, there was a <adjective> <noun> who <verb> in the <place>."

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    filled_story = story.replace("<adjective>", adjective) \
        .replace("<noun>", noun) \
        .replace("<verb>", verb) \
        .replace("<place>", place)

    print(filled_story)

mad_libs()

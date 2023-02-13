choices = ["conversion", "RAW_INTRO", "RAW_MENU_INTRO", "RAW_CHOOSE_CONVERSION_MENU", "RAW_CONVERSION_MENU",
           "RAW_END", "RAW_MK", "RAW_KM", "RAW_FC", "RAW_CF"]
while True:
    answer = input("What would you like to test?")
    if answer == "conversion":
        with open('pipeline.txt', 'w') as outfile:
            outfile.write("RAW\nMile\n.6\nKilometers\n1")
    elif answer == "RAW_INTRO":
        answer = "RAW_INTRO\n1"
        with open('pipeline.txt', 'w') as outfile:
            outfile.write(answer)
    else:
        with open('pipeline.txt', 'w') as outfile:
            outfile.write(answer)
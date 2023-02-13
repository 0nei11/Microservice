txt = {
    "RAW_MENU_INTRO": "COOKED\nTo go to the desired location, input the number associated with it.\n\n"
                      "1. Choose Conversion\n2. Random Conversion\n3. Exit",
    "RAW_CHOOSE_CONVERSION_MENU": "COOKED\nTo go to the desired conversion, input the number associated with it.\n"
                                  "Note: You can reverse the conversion direction for each given conversion.\n\n"
                                  "1. Miles to Kilometers\n2. Inches to Feet\n3. Fahrenheit to Celsius\n4. Back",
    "RAW_CONVERSION_MENU": "COOKED\nTo go to the action, input the number associated with it.\n\n"
                           "1. Enter value to convert.\n2. View conversion info.\n3. Reverse conversion direction.\n"
                           "4. Choose another conversion.\n5. Choose random conversion.\n6. Exit",
    "RAW_END": "COOKED\nThank you for using the conversion machine!",
    "RAW_MK": "COOKED\nMiles to Kilometers:\nGiven M = the Mile value we want to convert,\nThe "
              "formula is: M * 1.609344",
    "RAW_KM": "COOKED\nKilometers to Miles:\nGiven K = the Kilometer value we want to convert,\n"
              "The formula is: K / 1.609344",
    "RAW_FC": "COOKED\nFahrenheit to Celsius:\nGiven F = the Fahrenheit value we want to convert,\n"
              "The formula is: (F - 32) * (5/9)",
    "RAW_CF": "COOKED\nCelsius to Fahrenheit:\nGiven C = the Celsius value we want to convert,\n"
              "The formula is: C * (9/5) + 32"
}
while True:
    with open('pipeline.txt', 'r') as infile:
        run = infile.readline()
        run = run[0:len(run)]
        if run == "RAW\n":
            og_unit = infile.readline()
            og_value = infile.readline()
            new_unit = infile.readline()
            new_value = infile.readline()
            og_unit = og_unit[0:len(og_unit) - 1]
            og_value = og_value[0:len(og_value) - 1]
            new_unit = new_unit[0:len(new_unit) - 1]
            new_value = new_value[0:len(new_value)]
            with open('pipeline.txt', 'w') as outfile:
                outfile.write("COOKED\n" + og_value + " " + og_unit + "(s) is equal to " + new_value + " " + new_unit +
                              "(s).")
        if run == "RAW_INTRO\n":
            num = infile.readline()
            with open('pipeline.txt', 'w') as outfile:
                outfile.write("COOKED\nWelcome to the conversion machine!\nVersion " + str(num) + "\n"
                              "By - Jonathan Fernandez")
        elif run[0:4] == "RAW_":
            with open('pipeline.txt', 'w') as outfile:
                outfile.write(txt[run])

# Microservice
This microservice reads information from the file "pipeline.txt". The original program should alter the "pipeline.txt" file to one of the key words below on the first line when seeking certain text, cases involving more inputs are described below. The microservice writes COOKED on the first line to make sure each program knows what information is meant for who, and the actual program will write RAW at the start of the first line to let the microservice know it is it's turn to do an action.


3 use cases:
1.Basic text request with no customized input: (enter any of these keys and get the corresponding response).
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
2.RAW alone on the first line indicates a conversion was done and should be displayed. The second line is the original nit, third line is original value, fourth line is new unit, and fifth line is new value.
Example Input:
  RAW
  mile
  .6
  kilometer
  1
 Example Output:
  COOKED
  .6 mile(s) is equal to 1 kilometer(s)
  
3. RAW_INTRO alone on the first line indiates the intro with an intro with version number is being requested. THe second line of the txt file should say the version number.
Example Input:
  RAW_INTRO
  1
Example Output:
  COOKED
  Welcome to the conversion machine!
  Version 1
  By - Jonathan Fernandez
 
  

# WORKOUT TRACKER


## Description

This is a python command line application in which it will prompt you what exercises did you do today, and after you've written them in a plain english sentence, the application will read it and decifer what exercise did you do for how long and how many calories did it used.  For this application to work we need to pass in some parameters as environment variables

### Environment variables

- NUTRITION_API_KEY
    - For this app to work we will need to create a developer account in the [nutritionix API](http://developer.nutritionix.com) and when it's done we will get the api key
- NUTRITION_API_APPLICATION_ID
    - Once we've created the account we will get the app id
- NUTRITION_API_END_POINT
    - The api end point for the nutritionix api and it has to be https://trackapi.nutritionix.com/v2/natural
- NUTRITION_GENDER
    - The gender of the person who will be using the app
- NUTRITION_WEIGHT
    - The weight of the person in kg using the app
- NUTRITION_HEIGHT_CM
    - The height of the person in cm 
- NUTRITION_AGE
    - The age of the person
- SHEETY_API_END_POINT
    - You will need to create a new [sheety api](https://sheety.co/) by signing in with your google account, you must grant access to read and write to your spreadsheets in order for this app to work.  Once you are done creating the account you will need to create a project by giving it a link to an existing spreadsheet in your google drive and only then you will have your end point

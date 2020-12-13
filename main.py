from webbrowser import open_new
import os
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
import pytz
import datetime
import geograpy
import pyttsx3

# init function to get an engine instance for the speech synthesis  
engine = pyttsx3.init() 
engine.say('Hello! How may I help you?')
# run and wait method for processing the voice commands  
engine.runAndWait() 

#This is the code for the openning the websites
dict_of_websites = {"wikipedia": "https:\\www.wikipedia.org", "youtube":"https:\\www.youtube.com", "google":"https:\\www.google.com", "gmail":"https:\\www.gmail.com", "github":"https:\\www.gihtub.com", 'stack overflow':'https:\\www.stackoverflow.com', 'amazon':'https:\\www.amazon.in', 'flipkart':'https:\\www.flipkart.com'}
#This is the list of websites this program can open by default:
#wikipedia, youtube, google, gmail,github, stack overflow, amazon india, flipkart

def open_website(prompt):#Method used for opening a website
    prompt_list = prompt.split()
    for item in prompt_list:
        if item.lower() in dict_of_websites:
            open_new(dict_of_websites[item.lower()])
            return True
    return False

def add_website():#Method used for adding a website to the openable websites' list
    name = input("By what name do you want to open the website?")
    link = input("What is the URL of the website?")
    dict_of_websites[name] = link

def save_websites():
    if os.path.exists(os.path.dirname(os.path.realpath(__file__))+"websites_list.txt") == False:
        with open("websites_list.txt","w")as file:
            for item in dict_of_websites:
                file.write(item+ ","+dict_of_websites[item]+'\n')
    elif os.path.exists(os.path.dirname(os.path.realpath(__file__))+"websites_list.txt"):
        with open("websites_list.txt","a")as file:
            for item in dict_of_websites:
                file.write(item, ",",dict_of_websites[item],'\n')

def read_websites():
    global dict_of_websites
    with open("websites_list.txt","r") as file:
        websites = file.readlines()
        for item in websites:
            item.replace('\n','')
            website_name = item.split(',')[0]
            website_url = item.split(',')[1]
            dict_of_websites[website_name] = website_url

def display_time(prompt):
    #get the place in the prompt in the form of a list
    place = geograpy.get_place_context(text = prompt)

    #check if the place is in the list of countries, cities or regions
    if (place.countries or place.cities or place.regions):
        lad = input("Please enter the location again: ") #if a location is given, ask the user to enter the location again
    else: #if no location is given, ask the user to enter a location
        lad = input("Please enter the location: ")

    #initialize Nominatim API
    geolocator = Nominatim(user_agent = "geoapiExercises")

    #getting latitude and longitude
    location = geolocator.geocode(lad)

    #pass latitude and longitude to TimezoneFinder
    obj = TimezoneFinder()
    try:
        result = obj.timezone_at(lat = location.latitude, lng = location.longitude)
    except:
        print("Location not found")
        return
        
    #get the timezone
    time_zone = pytz.timezone(result)

    #get the date and time of the time zone
    time_date_now = datetime.datetime.now(time_zone)

    #display the time and date of the location
    print("Current time in ", lad, ":")
    print(time_date_now.strftime("%I:%M %p"))
    print(time_date_now.strftime("%A, %d %B %Y"))
    
#The following code is used to create to dos:


# This is the method that controls the entire program
def main():
    try:
        read_websites()
    except Exception as excep:
        pass
    prompt = input("Hi this is Baburao. How may i help you?")
    if 'time' in prompt.lower():
        display_time(prompt)
    if 'open' in prompt.lower():
        if open_website(prompt) == False:
            if 'Y' in input("No such website found in our list, do you want to add it to the list?").upper():
                add_website()
                save_websites()
    main()


main()

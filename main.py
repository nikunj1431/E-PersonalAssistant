from webbrowser import open_new

#This is the code for the openning the websites
dict_of_websites = {"wikipedia": "https:\\www.wikipedia.org", "youtube":"https:\\www.youtube.com", "google":"https:\\www.google.com", "gmail":"https:\\www.gmail.com", "github":"https:\\www.gihtub.com", 'stack overflow':'https:\\www.stackoverflow.com', 'amazon':'https:\\www.amazon.in', 'flipkart':'https:\\www.flipkart.com'}
#This is the list of websites this program can open by default:
#wikipedia
# youtube
# google
# gmail
# github
# stack overflow
# amazon india
# flipkart

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
    


#The following code is used to create to dos:


# This is the method that controls the entire program
def main():
    prompt = input("Hi this is Baburao. How may i help you?")
    if 'open' in prompt.lower():
        if open_website(prompt) == False:
            if 'Y' in input("No such website found in our list, do you want to add it to the list?").upper():
                add_website()
    main()


main()
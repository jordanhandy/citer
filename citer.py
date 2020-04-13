############################################################################
# Citer 
# version: 2.0
# Author: Jordan Handy

# Description
# Takes given input values and produces citation for bibliographies in:
# APA style for:
# books
# websites

############################################################################

# Citer ASCII Art 
f = open("log.txt","w")

print("""
      __________             
_________(_)_  /_____________
_  ___/_  /_  __/  _ \_  ___/
/ /__ _  / / /_ /  __/  /    
\___/ /_/  \__/ \___//_/     \n\n\n""")
print("Welcome to the Citer Application.  Given inputs, it outputs a citation")
input("Press enter to continue ... ")
print("[1] APA\n[2] MLA\n[3] Chicago")
style = input("Enter the style you'd like to cite in ")
if style == "1":
    print("[1] Book\n[2] Website\n[3] Journal\n[4] Video\n[5] Other ")
    citeType = input("What type of media would you like to cite? ")
    
    authorFirst = input("Enter the author's first name ").capitalize()
    authorLast = input("Enter the author's last name ").capitalize()
    pubYear = input("Enter the year of publication ")
    pubTitle = input("Enter the title of the work ")
    
    if citeType == "1":
        print("\nKEEP IN MIND:\nCapitalize the first letter of the first word of the title and any subtitles, as well as the first letter of any proper nouns.\nThe full title of the book, including any subtitles, should be stated and ITALICIZED.\n")
        pubTitle = ' '.join(word[0].upper() + word[1:] for word in pubTitle.split())
        pubCity = input("Enter the city of publication ")
        pubState = input("Enter the province / state of book publication ")
        publisher = input("Enter the name of the publisher ")
        print(f"Your citation is\n {authorLast}, {authorFirst[0]}. ({pubYear}). {pubTitle}. {pubCity}, {pubState}:{publisher}")
        print("Copy your citation.")
        input("Press enter to quit....")

    elif citeType == "2":
        pubMonth = input("Enter the month of publication ")
        pubDay = input("Enter the day of publication ")
        url = input("Enter the URL of the website ")
        if not authorFirst or not authorLast:
            print(f"Your citation is\n{pubTitle}. ({pubYear}, {pubMonth} {pubDay}). Retrieved from {url}")
            print("Copy your citation.")
            input("Press enter to quit....")
        else:
            print(f"Your citation is\n {authorLast}, {authorFirst[0]}. ({pubYear}, {pubMonth} {pubDay}). {pubTitle}. Retrieved from {url}")
            print("Copy your citation.")
            input("Press enter to quit....")
    
    elif citeType == "3":
        pubMonth = input("Enter the month of publication ")
        pubDay = input("Enter the day of publication ")
        pubPeriodTitle = input("Enter the Title of the Periodical ")
        pubPeriodTitle = ' '.join(word[0].upper() + word[1:] for word in pubPeriodTitle.split())
        volume = input("Enter the volume number ")
        issue = input("Enter the issue number ")
        pages = input("Enter the number range of pages referenced")

        print(f"Your citation is\n {authorLast}, {authorFirst[0]}. ({pubYear}. {pubTitle}. {pubPeriodTitle}, {volume}({issue}), {pages}")
        print("Copy your citation.")
        input("Press enter to quit....")
    
    elif citeType == "4":
        pubMonth = input("Enter the month of publication ")
        pubDay = input("Enter the day of publication ")
        url = input("Enter the URL of the website ")

        print(f"Your citation is\n {authorLast}, {authorFirst[0]}. ({pubYear}, {pubMonth}, {pubDay}). {pubTitle}. [Video file], Retreived from {url}")
        print("Copy your citation.")
        input("Press enter to quit....")
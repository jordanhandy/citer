############################################################################
# Citer 
# version: 2.1
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


#################################
# APA STYLE
#################################
if style == "1":
    print("[1] Book\n[2] Website\n[3] Journal\n[4] Video\n")
    citeType = input("What type of media would you like to cite? ")
    
    authorFirst = input("Enter the author's first name ").capitalize()
    authorLast = input("Enter the author's last name ").capitalize()
    pubYear = input("Enter the year of publication ")
    pubTitle = input("Enter the title of the work ")
    pubTitle = ' '.join(word[0].upper() + word[1:] for word in pubTitle.split())
    
    ###############################
    # APA STYLE - Book
    ###############################
    if citeType == "1":
        print("\nKEEP IN MIND:\nCapitalize the first letter of the first word of the title and any subtitles, as well as the first letter of any proper nouns.\nThe full title of the book, including any subtitles, should be stated and ITALICIZED.\n")

        pubCity = input("Enter the city of publication ")
        pubState = input("Enter the province / state of book publication ")
        publisher = input("Enter the name of the publisher ")
        print(f"Your citation is\n {authorLast}, {authorFirst[0]}. ({pubYear}). {pubTitle}. {pubCity}, {pubState}:{publisher}")
        print("Copy your citation.")
        input("Press enter to quit....")

    ###############################
    # APA STYLE - Website
    ###############################
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
    
    ###############################
    # APA STYLE - Journal
    ###############################
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
    
    ###############################
    # APA STYLE - Video
    ###############################
    elif citeType == "4":
        pubMonth = input("Enter the month of publication ")
        pubDay = input("Enter the day of publication ")
        url = input("Enter the URL of the website ")

        print(f"Your citation is\n {authorLast}, {authorFirst[0]}. ({pubYear}, {pubMonth}, {pubDay}). {pubTitle}. [Video file], Retreived from {url}")
        print("Copy your citation.")
        input("Press enter to quit....")

#################################
# MLA STYLE
#################################
if style == "2":
    print("[1] Book\n[2] Website\n[3] Journal\n[4] Video\n")
    citeType = input("What type of media would you like to cite? ")
    
    authorFirst = input("Enter the author's first name ").capitalize()
    authorLast = input("Enter the author's last name ").capitalize()
    pubYear = input("Enter the year of publication ")
    pubTitle = input("Enter the title of the work.  If this is a webpage, enter the page title ")
    pubTitle = ' '.join(word[0].upper() + word[1:] for word in pubTitle.split())

    ###############################
    # MLA STYLE - Book
    ###############################
    if citeType == "1":
        pubCity = input("Enter the city of publication ")
        publisher = input("Enter the name of the publisher")

        print(f"Your citation is\n {authorLast}, {authorFirst}. {pubTitle}. {pubCity}: {publisher}, {pubYear}. Print.")
        print("Copy your citation.")
        input("Press enter to quit....")

    ###############################
    # MLA STYLE - Website
    ###############################
    elif citeType == "2":
        print("\nKEEP IN MIND:\nThe title of the website needs to be ITALICIZED.\n")

        webTitle = input("Enter the name of the title of the entire website ")
        publisher = input("Enter the name of the publisher ")
        pubMonth = input("What month was it published ")
        pubDay = input("What day of the month (1,2,3....) ")
        url = input("Enter the URL of the site accessed")

        print(f"Your citation is\n {authorLast}, {authorFirst}. {pubTitle}. {webTitle}, {publisher}, {pubDay} {pubMonth} {pubYear}, {url}")
        print("Copy your citation.")
        input("Press enter to quit....")


    ###############################
    # MLA STYLE - Journal
    ###############################
    elif citeType == "3":
        journalTitle = print("Enter the title of the Journal")
        journalTitle = ' '.join(word[0].upper() + word[1:] for word in journalTitle.split())
        version = input("Enter version number. Press enter for none ")
        volume = input("Enter volume number.  Press enter for none ")
        pubMonth = input("Enter the month of publication ")
        pages = input("Enter the page numbers that were referenced ")
        contributors = input("Are there any other contributors? (y/n) ")
        
        if contributors == "y":
            contributorString = ""
            contName = input("Input the next name in the format (Last Name, First Name ")
            while contName != "done":
                contributorString += contName + " "
                contName = input("Input the next name in the format (Last Name, First Name ")
            else:
                contributorString = ""
        
        print(f"Your citation is\n {authorLast}, {authorFirst}. \"{pubTitle}\". {journalTitle}, {contributorString}, {version}, vol. {volume}, no {issue}, {pubMonth} {pubYear}, p.{pages}")
        print("Copy your citation.")
        input("Press enter to quit....")

    ###############################
    # MLA STYLE - Video
    ###############################
    elif citeType == "4":
        webTitle = input("Enter the title of the website where the video was found ")
        publisher = input("Enter the name of the video publisher / channel / creator ")
        pubMonth = input("Enter the mont that the video was published ")
        pubDay = input ("Enter the day the video was published ")
        url = input("Enter the URL where the video was found ")

        print(f"Your citation is\n {authorLast}, {authorFirst}, \"{pubTitle}\". {webTitle}, {publisher}, {pubDay} {pubMonth} {pubYear}, {url}.")
        print("Copy your citation.")
        input("Press enter to quit....")


#################################
# Chicago STYLE
#################################
if style == "3":
    print("[1] Book\n[2] Website\n[3] Journal\n[4] Video\n")
    citeType = input("What type of media would you like to cite? ")
    
    authorFirst = input("Enter the author's first name ").capitalize()
    authorLast = input("Enter the author's last name ").capitalize()
    pubYear = input("Enter the year of publication ")
    pubTitle = input("Enter the title of the work.  If this is a webpage, enter the page title ")
    pubTitle = ' '.join(word[0].upper() + word[1:] for word in pubTitle.split())

    ###############################
    # Chicago STYLE - Book
    ###############################
    if citeType == "1":
        print("\nKEEP IN MIND:\nThe title of the book needs to be ITALICIZED.\n")

        pubCity = input("Enter the city where the book was published")
        publisher = input("Enter the name of the publisher")

        print(f"Your citation is\n {authorLast}, {authorFirst}. {pubTitle}. {publisher}, {pubYear}.")
        print("Copy your citation.")
        input("Press enter to quit....")

    ###############################
    # Chicago STYLE - Website
    ###############################
    elif citeType == "2":
        webTitle = input("Enter the title of the entire website ")
        url = input("Enter the URL of the website ")
        pubMonth = input("Enter the month the website was accessed ")
        pubDay = input("Enter the date the website was accessed ")
         
        print(f"Your citation is\n {authorLast}, {authorFirst}. \"{pubTitle}.\" {webTitle}. {url} (retrieved {pubMonth} {pubDay} {pubYear}).")        
        print("Copy your citation.")
        input("Press enter to quit....")

    ###############################
    # Chicago STYLE - Journal
    ###############################
    elif citeType == "3":
        journalTitle = input("Enter the title of the journal ")
        volume = input("Enter the volume number ")
        pages = input("Enter page ranges ")
    
        print(f"Your citation is\n {authorLast}, {authorFirst}. \"{pubTitle}.\" {journalTitle}, no {volume} ({pubYear}). {pages}.")
        print("Copy your citation.")
        input("Press enter to quit....")
    
    ###############################
    # Chicago STYLE - Video
    ###############################
    elif citeType == "4":
        time = input("Enter video duration in mm:ss ")
        url = input("Enter the url of the video ")
        pubMonth = input("Enter the month of publication ")
        accessedMonth = input("The month you viewed the video ")
        accessedYear = input("The year you viewed the video ")

        print(f"Your citation is\n {authorLast}, {authorFirst}. \"{pubTitle}\". Filmed [{pubMonth} {pubYear}. YouTube video, {time} Posted [{accessedMonth} {accessedYear}]. {url}.")
        print("Copy your citation.")
        input("Press enter to quit....")
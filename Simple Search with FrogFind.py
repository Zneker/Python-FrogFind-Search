import webbrowser as web

search = "?q="+(input("What would you like to search: "))

web.open_new_tab("https://www.frogfind.com"+search)


import urllib.parse
import requests

import tkinter as tk
from tkinter import simpledialog
from tkinter import *

ROOT = tk.Tk()
ROOT.withdraw()

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "1Lj1KgtsunN0Hrh4MSelYCVd3yVmKx90"

while True:

    orig = simpledialog.askstring(title="MapQuest",
                                  prompt="Starting Location: \t\t\t\t\t\t")
    if orig == "quit" or orig == "q":
        print("\u001b[31;1mExiting the program...\u001b[0m")
        break
    dest = simpledialog.askstring(title="MapQuest",
                                  prompt="Destination: \t\t\t\t\t\t")
    if dest == "quit" or dest == "q":
        print("\u001b[31;1mExiting the program...\u001b[0m")
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    json_data = requests.get(url).json()

    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        root = tk.Tk()

        root.geometry("600x500")
        root['background'] = '#36bfaf'
        root.title('MapQuest')

        # Add a Scrollbar(horizontal)
        v = Scrollbar(root, orient='vertical')
        v.pack(side=RIGHT, fill='y')
        # add label
        l = Label(root, text=orig + " to " + dest)
        l.config(font=("Courier", 14))

        text = tk.Text(root, selectbackground="grey", yscrollcommand=v.set)
        text.insert(INSERT, "API Status: " + str(json_status) + " A successful route call. \n")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            text.insert(INSERT, str(each["narrative"]) + " (" + str(each["distance"] * 1.61) + " km) \n")
        l.pack()
        text.pack()

        # Attach the scrollbar with the text widget
        v.config(command=text.yview)

        root.mainloop()
    elif json_status == 402:
        print("**********************************************")
        print(
            "\u001b[31mStatus Code: " + str(json_status) + "\u001b[0m; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("\u001b[31mStatus Code: " + str(json_status) + "\u001b[0m; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("\u001b[31mFor Staus Code: " + str(json_status) + "\u001b[0m; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
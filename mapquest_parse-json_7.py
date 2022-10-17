import urllib.parse
import requests

import tkinter as tk
from tkinter import simpledialog

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
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()

    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print("\n\u001b[36;1mAPI Status: " + str(json_status) + " =\u001b[32;1m A successful route call.\u001b[0m")
        print("=============================================")
        print("\u001b[36;1mDirections from \u001b[0m" + "\u001b[32;1m" + (orig) + "\u001b[0m" + "\u001b[36;1m to \u001b[0m" + "\u001b[32;1m" + (dest) + "\u001b[0m" )
        print("\u001b[36;1mTrip Duration: " + "\u001b[32;1m" + (json_data["route"]["formattedTime"]) + "\u001b[0m")
        print("\u001b[36;1mKilometers: " + "\u001b[32;1m" + str("{:.2f}".format((json_data["route"]["distance"])*1.61)) + "\u001b[0m")
        print("\u001b[36;1mFuel Used (Ltr): " + "\u001b[32;1m" + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)) + "\u001b[0m")
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print("\u001b[36;1m"+str((each["narrative"])) + " \u001b[33;1m(" + str("{:.2f}".format((each["distance"])*1.61) + "km) " + "\u001b[31;1m"+str(each[("formattedTime")])+"\u001b[0m"))
        print("=============================================\n")
    elif json_status == 402:
        print("**********************************************")
        print("\u001b[31mStatus Code: " + str(json_status) + "\u001b[0m; Invalid user inputs for one or both locations.")
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
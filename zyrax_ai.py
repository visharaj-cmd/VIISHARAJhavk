import os

def chat():
    while True:
        user = input("ZyraX> ").lower()

        if user == "exit":
            print("Shutting down ZyraX...")
            break

        elif "wifi" in user:
            print("Running WiFi Analyzer Module")

        elif "network" in user:
            print("Running Network Scanner")

        elif "system" in user:
            print("Checking system status")

        elif "tools" in user:
            print("""
Available Tools:
wifi
network
system
exit
""")

        else:
            print("Command not recognized")

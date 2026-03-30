from rich.console import Console

console = Console()

def chat():

    while True:
        user = input("ZyraX> ").lower()

        if user == "exit":
            console.print("Shutting down ZyraX", style="red")
            break

        elif "wifi" in user:
            console.print("Running WiFi Analyzer", style="green")

        elif "network" in user:
            console.print("Running Network Scanner", style="green")

        elif "system" in user:
            console.print("Checking System", style="green")

        elif "tools" in user:
            console.print("""
Available Tools:
wifi
network
system
exit
""")

        else:
            console.print("Command not recognized", style="yellow")

from Mailgun import Mailgun
import numpy as np


def main():
    print("Starting game")
    spyfall_round(first_round=True)
    while True:
        spyfall_round()
        answer = yes_or_no()
        print(answer)
        if not answer:
            break
        


def yes_or_no(prompt = "Noch eine Runde? [j/n]:"):
    while True:
        try:
            ans = input(prompt)
        except (EOFError, KeyboardInterrupt):
            print()
            return False
        if ans == "j":
            return True
        else:
            return False



def spyfall_round(first_round = None): 
    email_adresses = ["leunam.schule@gmail.com"]

    number_of_players = len(email_adresses)

    locations = [
    "Beach",
    "Broadway Theater",
    "Casino",
    "Circus Tent",
    "Bank",
    "Day Spa",
    "Hotel",
    "Restaurant",
    "Supermarket",
    "Service Station",
    "Hospital",
    "Embassy",
    "Military Base",
    "Police Station",
    "School",
    "University",
    "Airplane",
    "Ocean Liner",
    "Passenger Train",
    "Submarine",
    "Cathedral",
    "Corporate Party",
    "Movie Studio",
    "Crusader Army",
    "Pirate Ship",
    "Polar Station",
    "Space Station",
]

    selected_location = locations[np.random.randint(0, len(locations))]

    spy = np.random.randint(0, number_of_players, 1)


    spy_text = f"You are the spy, try to guess where the detectives are!"
    spy_mail = Mailgun(subject = "Spyfall", text = spy_text)

    detective_text = f"You are the detective, try to find the spy! You are at the {selected_location}."
    detective_mail = Mailgun(subject="Spyfall", text=detective_text)
    if first_round == True:
        initial_text = f"Welcome to spyfall! Lets find the spy or try to not get caught as such. Below are the possible locations for this game.{locations}"
        initial_mail = Mailgun(subject = "Locations", text = initial_text)
        for player in range(number_of_players):
            email_adress = email_adresses[player]
            initial_mail.email_adress = email_adress
            initial_mail.gmail_send_message()
        return 

    for player in range(number_of_players):
        if player != spy:
            email_adress = email_adresses[player]
            detective_mail.email_adress = email_adress
            detective_mail.gmail_send_message()
        else:
            email_adress = email_adresses[player]
            spy_mail.email_adress = email_adress
            spy_mail.gmail_send_message()
    

if __name__ ==  "__main__":
    main()
















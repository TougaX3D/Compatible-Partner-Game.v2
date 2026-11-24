class Player:
    def __init__(self, mental_health=100, money=600):
        self.mental_health = mental_health
        self.money = money


class Candidate:
    def __init__(self, name, age, vibe, pros, cons, affection):
        self.name = name
        self.first_name = name.split()[0]
        self.age = age
        self.vibe = vibe
        self.pros = pros
        self.cons = cons
        self.affection = affection

    def show_profile(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Vibe: {self.vibe}")
        print(f"Pros: {', '.join(self.pros)}")
        print(f"Cons: {', '.join(self.cons)}")
        print(f"Starting Affection: {self.affection}/100\n")


class ChillGirl(Candidate):
    def __init__(self, name, age, vibe, pros, cons, ghost_chance=30):
        super().__init__(name, age, vibe, pros, cons, affection=50)
        self.ghost_chance = ghost_chance


class AcademicGirl(Candidate):
    def __init__(self, name, age, vibe, pros, cons, study_stress=40):
        super().__init__(name, age, vibe, pros, cons, affection=50)
        self.study_stress = study_stress


class StreetsGirl(Candidate):
    def __init__(self, name, age, vibe, pros, cons, roster_count=4):
        super().__init__(name, age, vibe, pros, cons, affection=50)
        self.roster_count = roster_count


while True:
    print("---------------------------------------------------")
    print(" Goodday! This is the Compatible Partner Game!!!")
    print("---------------------------------------------------\n")
    print("In this game you find which girl is most compatible with you, and you pick them to be your partner!!!")
    ans = input("Do you wanna play the game? (Y/N): ").upper()

    if ans == "Y":
        # Fresh objects every round so stats reset if you play again
        player = Player()

        candidate1 = ChillGirl(
            name="Candice Dal Awanoras",
            age=16,
            vibe="chill",
            pros=["pretty", "matching music tastes", "no baggage"],
            cons=["replies late", "low eq"]
        )

        candidate2 = AcademicGirl(
            name="Hali Maw Magaral",
            age=17,
            vibe="passionate",
            pros=["cute", "academic achiever", "nerdy", "high eq & iq"],
            cons=["focused on acads"]
        )

        candidate3 = StreetsGirl(
            name="Shea S Notakiper",
            age=19,
            vibe="attention - seeking",
            pros=["sexy", "beautiful", "clingy", "high eq"],
            cons=["in multiple situationships", "emotional instability"]
        )

        print("\n--- Candidate 1 ---")
        candidate1.show_profile()

        print("--- Candidate 2 ---")
        candidate2.show_profile()

        print("--- Candidate 3 ---")
        candidate3.show_profile()

        # 1. Pick your candidate
        while True:
            ans2 = input("Please enter which candidate to choose as your partner!!! (1/2/3): ")
            if ans2 == "1":
                chosen_girl = candidate1
                break
            elif ans2 == "2":
                chosen_girl = candidate2
                break
            elif ans2 == "3":
                chosen_girl = candidate3
                break
            else:
                print("\nYou did not input correctly! Please choose between (1/2/3)\n")

        print("\n------------------------------------------------------------")
        print(f"You locked in {chosen_girl.first_name}! Let's see how the next 5 days go...")
        print("--------------------------------------------------------------")

        # 2. 5-Day Relationship Loop
        for day in range(1, 6):
            print(f"\n--- DAY {day} | Money: ₱{player.money} | Mental: {player.mental_health}% | Affection: {chosen_girl.affection}/100 ---")
            print("1. Take her out (-₱300) | 2. Text / Hang out (Free) | 3. Grind / Hoop (+Mental)")
            move = input("Choice (1/2/3): ")

            if move == "1" and player.money >= 300:
                player.money -= 300
                chosen_girl.affection += 10
                print(f"Good date with {chosen_girl.first_name}! Affection +10.")
            elif move == "2":
                player.money += 150
                chosen_girl.affection += 8
                if isinstance(chosen_girl, StreetsGirl):
                    player.mental_health -= 50
                    print(f"Hung out with {chosen_girl.first_name}, but she was texting 3 other guys. Mental -50!")
                elif isinstance(chosen_girl, ChillGirl):
                    player.mental_health -= 30
                    print(f"{chosen_girl.first_name} took 2 hours to reply to every text. Mental -30!")
                else:
                    player.mental_health -= 5
                    print(f"Chill study call with {chosen_girl.first_name}. Affection +8, Mental -5.")
            elif move == "3":
                player.money += 150
                player.mental_health = min(100, player.mental_health + 50)
                chosen_girl.affection -= 5
                print("Locked in on coding and hoops. Mental health recovered!")
            else:
                print("Invalid move or not enough cash! Day wasted.")

            if player.mental_health <= 0:
                print("\n-----------------------------------------------------------------------------")
                print("BURNOUT ENDING: Your mental health hit 0. You took a break from dating.")
                print("-----------------------------------------------------------------------------")
                break
        else:
            if chosen_girl.affection >= 80:
                print("\n-------------------------------------")
                print(f"YOU WON! Locked in with {chosen_girl.first_name}!")
                print("-------------------------------------")
            else:
                print("\n-------------------------------------------------------------")
                print(f"FRIENDZONED! {chosen_girl.first_name} said 'let's just be friends.'")
                print("--------------------------------------------------------------")

        again = input("\nPlay again? (Y/N): ").upper()
        if again != "Y":
            print("Thanks for playing!")
            break
    else:
        print("Maybe next time!")
        break

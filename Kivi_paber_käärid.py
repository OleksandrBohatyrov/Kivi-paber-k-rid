import random
mylist = ["paber", "kivi", "kaarid"]

player_round_wins=0
bot_round_wins=0
draws=0
rounds=int(input("Mitu vooru sa mängida tahad? "))

for i in range(rounds):
    print(f"Round {i + 1}: ")
    while True:
        player = input("paber, kivi, or kaarid: ").lower()
        if player.isdigit:
            print("Value Error")
            player = input("paber, kivi, or kaarid: ").lower()
        break
    bot = random.choice(mylist)
    print(f"Bot chose {bot}")

    if player == bot:
        print("Viik.")
        draws += 1
    elif (player == "kivi" and bot == "kaarid") or (player == "paber" and bot == "kivi") or (player == "kaarid" and bot == "paber"):
        print("Sina võitsid.")
        player_round_wins += 1
    else:
        print("Bot võitsid.")
        bot_round_wins += 1


print()
print(f"Sa võitsid {player_round_wins} voorud",f" bot võitsid {bot_round_wins}")
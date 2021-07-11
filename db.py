def read_player_money():
    try:
        player_money = []
        with open("player_money.txt") as file:
            for line in file:
                line = line.replace("\n", "")
                player_money.append(line)
            return player_money
    except FileNotFoundError as e:
        player_money = [100]
        return player_money

def write_player_money(player_money):
    #player_money = str(player_money)
    with open("player_money.txt", "w") as file:
        #for item in player_money:
        file.write(str(player_money) + "\n")
        return player_money   

def return_player_money():
    with open("player_money.txt") as file:
        for line in file:
            player_money = int(line)
            return player_money
    

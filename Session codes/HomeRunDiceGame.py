import random

def roll_dice():
    return random.randint(1, 6)

def move_player(player, steps):
    player["position"] += steps
    if player["position"] > 30:
        player["position"] = 30
    print(f"Player {player['name']} is now at position {player['position']}")

def reset_player(player):
    player["position"] = 0

def check_collision(player1, player2):
    if player1["position"] == player2["position"]:
        print(f"Player {player1['name']} collided with Player {player2['name']}!")
        reset_player(player2)
        return True
    return False

def play_game():
    player1 = {"name": "1", "position": 0}
    player2 = {"name": "2", "position": 0}
    current_player = player1

    while True:
        input(f"It's Player {current_player['name']}'s turn. Press Enter to roll the dice.")
        dice_roll = roll_dice()
        print(f"Player {current_player['name']} rolled a {dice_roll}.")

        if dice_roll == 6:
            print(f"Player {current_player['name']} gets an additional move!")
            dice_roll = roll_dice()
            print(f"Player {current_player['name']} rolled a {dice_roll}.")

        move_player(current_player, dice_roll)

        if check_collision(player1, player2):
            move_player(current_player, dice_roll)

        if current_player["position"] == 30:
            print(f"Player {current_player['name']} reached the finish line!")
            print(f"Player {current_player['name']} wins the game!")
            break

        if current_player == player1:
            current_player = player2
        else:
            current_player = player1

play_game()

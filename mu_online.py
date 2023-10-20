dungeon_rooms = input().split("|")

game_won = True
health = 100
bitcoins = 0
current_room_number = 0

for room in dungeon_rooms:
    commands = room.split()
    command = commands[0]
    number = int(commands[1])
    current_room_number += 1

    if command == "potion":
        last_health = health
        health += number
        if health > 100:
            health = 100
        print(f"You healed for {health - last_health} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        monster = command
        health -= number
        if health > 0:
            print(f"You slayed {monster}.")
        else:
            print(f"You died! Killed by {monster}.")
            print(f"Best room: {current_room_number}")
            game_won = False
            break

if game_won:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
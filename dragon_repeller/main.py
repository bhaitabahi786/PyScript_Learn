import random
from pyscript import document, display

xp = 0
health = 100
gold = 50
currentWeapon = 0
fighting = None
monsterHealth = None
inventory = ["stick"]

button1 = document.querySelector("#button1")
button2 = document.querySelector("#button2")
button3 = document.querySelector("#button3")
text = document.querySelector("#text")
xpText = document.querySelector("#xpText")
healthText = document.querySelector("#healthText")
goldText = document.querySelector("#goldText")
monsterStats = document.querySelector("#monsterStats")
monsterName = document.querySelector("#monsterName")
monsterHealthText = document.querySelector("#monsterHealth")

weapons = [
    {"name": "stick", "power": 5},
    {"name": "dagger", "power": 30},
    {"name": "claw hammer", "power": 50},
    {"name": "sword", "power": 100}
]

monsters = [
    {"name": "slime", "level": 2, "health": 15},
    {"name": "fanged beast", "level": 8, "health": 60},
    {"name": "dragon", "level": 20, "health": 300}
]

locations = [
    {
        "name": "town square",
        "button_text": ["Go to store", "Go to cave", "Fight dragon"],
        "text": "You are in the town square. You see a sign that says 'Store'.",
    },
    {
        "name": "store",
        "button_text": ["Buy 10 health (10 gold)", "Buy weapon (30 gold)", "Go to town square"],
        "text": "You enter the store.",
    },
    {
        "name": "cave",
        "button_text": ["Fight slime", "Fight fanged beast", "Go to town square"],
        "text": "You enter the cave. You see some monsters.",
    },
    {
        "name": "fight",
        "button_text": ["Attack", "Dodge", "Run"],
        "text": "You are fighting a monster."
    },
    {
        "name": "lose",
        "button_text": ["REPLAY?", "REPLAY?", "REPLAY?"],
        "text": "You die. ☠️"
    },
    {
        "name": "win",
        "button_text": ["REPLAY?", "REPLAY?", "REPLAY?"],
        "text": "You defeat the dragon! YOU WIN THE GAME! 🎉"
    },
    {
        "name": "easter egg",
        "button_text": ["2", "8", "Go to town square?"],
        "text": "You find a secret game. Pick a number above. Ten numbers will be randomly chosen between 0 and 10. If the number you choose matches one of the random numbers, you win!"
    },
    {
        "name": "kill monster",
        "button_text": ["Go to town square", "Go to town square", "Go to town square"],
        "text": "The monster screams Arg! as it dies. You gain experience points and find gold."
    },
]

def update(location) :
    monsterStats.style.display = "none"
    text.innerHTML = location["text"]
    button1.innerText = location["button_text"][0]
    button2.innerText = location["button_text"][1]
    button3.innerText = location["button_text"][2]
    

def go_store(event):
    update(locations[1])
    button1.onclick =  buy_health
    button2.onclick =  buy_weapon
    button3.onclick =  go_town


def go_town(event):
    update(locations[0])
    
    button1.onclick =  go_store
    button2.onclick =  go_cave
    button3.onclick =  fight_dragon


def go_cave(event):
    update(locations[2])
    button1.onclick =  fight_slime
    button2.onclick =  fight_beast
    button3.onclick =  go_town


def goFight(monster):
    global monsterHealth
    update(locations[3])

    monsterHealth = monsters[monster]["health"]
    print(f"monster health of line 1 : {monsterHealth}")
    
    monsterStats.style.display = "block"
    monsterName.innerText = monsters[monster]["name"]
    monsterHealthText.innerText = monsterHealth

    button1.onclick =  attack
    button2.onclick =  dodge
    button3.onclick =  go_town
 


def fight_slime(event):
    global fighting
    fighting = 0
    goFight(fighting)

def fight_beast(event):
    global fighting
    fighting = 1
    goFight(fighting)

def fight_dragon(event):
    global fighting
    fighting = 2
    goFight(fighting)

def attack(event):
    global monsterHealth, fighting, health, gold, xp

    if health > 0:

        print(f"monster health after value : {monsterHealth}")
        print(f"current weapon : {currentWeapon}")
        print(f"weapons : {weapons[currentWeapon]['power']}")
        monsterHealth -= weapons[currentWeapon]["power"]
        print(f"under attack : {monsterHealth}")
        monsterHealthText.innerText = monsterHealth
        gold += 15
        xp += 10
        health -= 10
        healthText.innerHTML = health
        goldText.innerHTML = gold
        xpText.innerHTML = xp

        if monsterHealth < 0:

            update(locations[7])
            button1.onclick = go_town
            button2.onclick = go_town
            button3.onclick = easter_egg

    else:
        text.innerHTML = "Your health is 0 go buy it !!!."


button1.onclick = go_store
button2.onclick = go_cave
button3.onclick = fight_dragon

def buy_health(event):
    global health, gold
    if gold >= 10:
        health += 10
        gold -= 10
        healthText.innerHTML = health
        goldText.innerHTML = gold
    else:
        text.innerHTML = "You don't have enough gold."

def buy_weapon(event):
    global gold, currentWeapon

    if currentWeapon == 3:
        text.innerHTML = "You already have the best weapon."
    else:

        if gold >= 30:
            currentWeapon += 1
            gold -= 30
            goldText.innerHTML = gold
        else:
            text.innerHTML = "You don't have enough gold."

def dodge(event):
    global health
    health -= 10
    healthText.innerHTML = health

def restart(event):
    global xp, health, gold, currentWeapon
    xp = 0
    health = 100
    gold = 50
    currentWeapon = 0
    update(locations[0])
    xpText.innerHTML = xp
    healthText.innerHTML = health
    goldText.innerHTML = gold
    button1.onclick = go_store
    button2.onclick = go_cave
    button3.onclick = fight_dragon

def easter_egg(event):
    update(locations[6])
    button1.onclick = pick_two
    button2.onclick = pick_eight
    button3.onclick = go_town

def pick_two(event):
    global xp, gold
    number = random.randint(1, 10)
    if number == 2:
        text.innerHTML = "You win! You get 100 gold and 50 xp."
        gold += 100
        xp += 50
        goldText.innerHTML = gold
        xpText.innerHTML = xp
    else:
        text.innerHTML = "You lose. Try again."

def pick_eight(event):
    global xp, gold
    number = random.randint(1, 10)
    if number == 8:
        text.innerHTML = "You win! You get 100 gold and 50 xp."
        gold += 100
        xp += 50
        goldText.innerHTML = gold
        xpText.innerHTML = xp
    else:
        text.innerHTML = "You lose. Try again."

def lose(event):
    update(locations[4])
    button1.onclick = restart
    button2.onclick = restart
    button3.onclick = restart

def win(event):
    update(locations[5])
    button1.onclick = restart
    button2.onclick = restart
    button3.onclick = restart



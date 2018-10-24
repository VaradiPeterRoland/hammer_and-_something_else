from time import sleep
import sys
import random
import os

print("""⢀⢀⢀⢀⢀⢀⢀⢀⢀⠶⣿⣭⡧⡤⣤⣻⣛⣹⣿⣿⣿⣶⣄
⢀⢀⢀⢀⢀⢀⢀⢀⢀⣼⣊⣤⣶⣷⣶⣧⣤⣽⣿⣿⣿⣿⣿⣿⣷
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⢀⢀⢀⢀⢀⢀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧
⢀⢀⢀⢀⢀⢀⠸⠿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣻⣿⣿⣿⣿⣿⡆
⢀⢀⢀⢀⢀⢀⢀⢸⣿⣿⡀⠘⣿⡿⢿⣿⣿⡟⣾⣿⣯⣽⣼⣿⣿⣿⣿⡀
⢀⢀⢀⢀⢀⢀⡠⠚⢛⣛⣃⢄⡁⢀⢀⢀⠈⠁⠛⠛⠛⠛⠚⠻⣿⣿⣿⣷
⢀⢀⣴⣶⣶⣶⣷⡄⠊⠉⢻⣟⠃⢀⢀⢀⢀⡠⠔⠒⢀⢀⢀⢀⢹⣿⣿⣿⣄⣀⣀⣀⣀⣀⣀
⢠⣾⣿⣿⣿⣿⣿⣿⣿⣶⣄⣙⠻⠿⠶⠒⠁⢀⢀⣀⣤⣰⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄
⢿⠟⠛⠋⣿⣿⣿⣿⣿⣿⣿⣟⡿⠷⣶⣶⣶⢶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢀⢀⢀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠉⠙⠻⠿⣿⣿⡿
⢀⢀⢀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢀⢀⢀⢀⠈⠁
⢀⢀⢀⢀⢸⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⢀⢀⢀⢀⢸⣿⣿⣿⣿⣄⠈⠛⠿⣿⣿⣿⣿⣿⣿⣿⡿⠟⣹⣿⣿⣿⣿⣿⣿⣿⣿⠇
⢀⢀⢀⢀⢀⢻⣿⣿⣿⣿⣧⣀⢀⢀⠉⠛⠛⠋⠉⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⠏
⢀⢀⢀⢀⢀⢀⢻⣿⣿⣿⣿⣿⣷⣤⣄⣀⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋
⢀⢀⢀⢀⢀⢀⢀⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢹⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁
⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⣿⡇⢀⠈⠙⠛⠛⠛⠛⠛⠛⠻⣿⣿⣿⠇
⢀⢀⢀⢀⢀⢀⢀⢀⢀⣸⣿⡇⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢨⣿⣿
⢀⢀⢀⢀⢀⢀⢀⢀⣾⣿⡿⠃⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢸⣿⡏
⢀⢀⢀⢀⢀⢀⢀⢀⠻⠿⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢀⢠⣿⣿⡇""")

def cool_typing(line):
    for x in line:
        print(x, end='')
        sys.stdout.flush()
        sleep(0.1)


def get_Knuckle_Name(name):
    name = input()
    return name


def Hero():
    hero_hp = 1000
    hero_dmg = 10
    hero_inventory = ['Sword']
    return hero_hp, hero_dmg, hero_inventory


def Wild_Unicorn(knuckle_name):
    cool_typing('While you were wanderin in that place a Wild Unicorn appeared in front of you \n' + knuckle_name + " wants to fight the Unicorn so he/she/other starts spiting on it")
    monster_hp = 1
    monster_dmg = 1
    monster_inventory = ["Sweater of the Mighty Owen", "a tasty muffin"]
    return monster_hp, monster_dmg, monster_inventory


def start_game(starting_answer):
    starting_answer = input()
    if starting_answer == 'yes' or starting_answer == 'Yes' or starting_answer == 'Y' or starting_answer == 'y':
        os.system('clear')
        cool_typing('very noice then i will fallow ya!\n')
        knuckle_name = get_Knuckle_Name(cool_typing('*Your new companion havent got a name yet*\n Name him/her/other: '))
        random_way(knuckle_name)
        return knuckle_name
    else:
        cool_typing('*The knuckle spits on you then runs away*\n GAME OVER!\n')
        sys.exit()


def random_way(knuckle_name):
    cool_typing('*There are 2 ways ahead of you and ' + knuckle_name + '\n Which one do you chose?(1/2): \n')
    chose_way = input()
    if chose_way == '1':
        Meme_Forest(knuckle_name)
    elif chose_way == '2':
        pass
    else:
        cool_typing('*The knuckle spits on you then runs away*\n GAME OVER!\n')
        sys.exit()


def Meme_Forest(knuckle_name):
    cool_typing('You and ' + knuckle_name + ' entered The forest of Memes \n')
    monster = Wild_Unicorn(knuckle_name)
    hero = Hero()
    fight_system(monster_dmg, monster_hp, hero_dmg, hero_hp)


def fight_system(m_dmg, m_hp, h_dmg, h_hp):
    monster_hp = monster
    hero_hp = hero

    for turn in range(10):
        hit_or_miss = random.randint(1, 10)
        if hit_or_miss == 1 or hit_or_miss == 2 or hit_or_miss == 3 or hit_or_miss == 4 or hit_or_miss == 5:
            monster_hp -= hero_dmg
            cool_typing('You hit the Unicorn for ', hero_dmg, ' damage')
            if monster_hp <= 0:
                cool_typing('You killed the Unicorn!')
                continue
        else:
            hero_hp -= monster_dmg
            cool_typing('You missed so the Unicorn hits you', monster_dmg, 'damage.\nYour hp is: ', hero_hp)
            if hero_hp <= 0:
                cool_typing('*You died and the knuckle spits on you then runs away*\n GAME OVER!\n ')
                sys.exit()


def main():
    start_game(cool_typing('Hello adventurer! Do ya knaw da wae? \n Yes / No: '))


if __name__ == '__main__':
    main()

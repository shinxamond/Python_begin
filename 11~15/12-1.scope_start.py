enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Scope(전역변수)
player_health = 10

def drink_potion():
    #Local Scope(지역변수)
    potion_strength = 2
    print(potion_strength)
    print(player_health)


drink_potion()
#print(potion_strength) -> NameError
print(player_health)

# 변수뿐만이 아니라 함수나 기타 개념에도 scope가 적용된다
# def game():
#   def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#     print(player_health)
#
#   drink_potion() -> o
#
# drink_potion() -> x


# There is no Block Scope in Python
game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    print(new_enemy)


# Modifying Global Scope : 전역변수를 직접 수정하지 말고 return을 이용
enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


#Global Constants
PI = 3.14159
URL = "https://www.google.com"
TWITTER_HANDLE = "@layla"
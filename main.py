from termcolor import cprint
from roboter import utils


def askName():

    while True:
        cprint("Hello, I'm Meow. What is your name?", "cyan",
               attrs=["bold", "reverse"])
        cprint("> ", end="")

        global username
        username = input().capitalize()
        if username:
            break
        cprint("Oops, Please input again.", "red")

def recommendRestaurants(dic):
    print("R", dic)

    for name, count in dic.items():
        cprint(f"{username}, I recommend {name} restaurant." +
               f"[♥{count}]"
               f" Do you like? [y/n]", "cyan", attrs=["bold", "reverse"])
        cprint("> ", end="")

        bools = {"y": True, "yes": True, "n": False, 'no': False}
        while True:
            is_liked = bools.get(input("").lower(), -1)
            if type(is_liked) is bool:
                break
            cprint("Oops, Please input again.", "red")
            cprint("> ", end="")

        if is_liked:
            dic[name] = int(dic[name]) + 1


def askRestaurant(dic):
    cprint(f"{name}, Witch restaurants do you like?", "cyan",
           attrs=["bold", "reverse"])
    cprint("> ", end="")
    restaurant = input()


    cprint(f"Thank you so much, {name}!"
           " Have a good day!", "cyan",
           attrs=["bold", "reverse"])

def main():

    askName()

    filename = "restaurants_ranking.csv"
    fieldnames = ["name", "count"]
    dic = utils.read_csv(filename)
    # print("R", dic)

    recommendRestaurants(dic)

    askRestaurant(dic)

    newdic = {}
    print("U", newdic)
    dic.update(newdic)

    print("W", dic)
    utils.write_csv(filename, fieldnames, dic)

main()
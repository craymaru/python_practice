import csv

from termcolor import cprint

# while True:
#     cprint("Hello, I'm Meow. What is your name?", "cyan",
#            attrs=["bold", "reverse"])
#     cprint("> ", end="")
#     name = input().capitalize()
#     if name:
#         break
#     cprint("Oops, Please input again.", "red")
#
#
# with open("restaurants_ranking.csv", "r") as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         cprint(f"{name}, I recommend {row['name']} restaurant."
#                "Do you like? [y/n]", "cyan", attrs=["bold", "reverse"])
#         cprint("> ", end="")
#
#         dic = {"y": True, "yes": True, "n": False, 'no': False}
#         while True:
#             inputs = dic.get(input("").lower(), -1)
#             if type(inputs) is bool:
#                 break
#             cprint("Oops, Please input again.", "red")
#             cprint("> ", end="")
#
# cprint(f"{name}, Witch restaurants do you like?", "cyan",
#        attrs=["bold", "reverse"])
# cprint("> ", end="")
# restaurant = input()
#
#
# cprint(f"Thank you so much, {name}!"
#        " Have a good day!", "cyan",
#        attrs=["bold", "reverse"])
#
# with open("restaurants_ranking.csv", "w") as csv_file:
#     fieldnames = ["name", "count"]
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#
#
# with open("restaurants_ranking.csv", "a") as csv_file:
#     if :
#         fieldnames = ["name", "count"]
#         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#         writer.writeheader()
#     num = 0
#     num += 1
#     writer.writerow({"name": restaurant, "count": num})
#


def read_csv(filename):
    with open(filename, newline = "") as f:
        read_dict = csv.DictReader(f, delimiter=",", quotechar='"')
        return_dict = read_dict
        ks = read_dict.fieldnames
        return_dict = {k: [] for k in ks}

        for row in read_dict:
            for k, v in row.items():
                return_dict[k].append(v) # notice the type of the value is always string.

    return return_dict


def write_csv(filename, save_dict):
    save_row = {}

    with open(filename,'w') as f:
        writer = csv.DictWriter(f, fieldnames=save_dict.keys(),delimiter=",",quotechar='"')
        writer.writeheader()

        k1 = list(save_dict.keys())[0]
        length = len(save_dict[k1])

        for i in range(length):
            for k, vs in save_dict.items():
                save_row[k] = vs[i]

            writer.writerow(save_row)


# def appendNewRow(dict, name, count=1):
#     dict["name"].append(name)
#     dict["count"].append(count)
#     return

# def patchRow(dict):
#     dict["count"]

def main():
    filename = "restaurants_ranking.csv"
    dict = read_csv(filename)
    appendNewRow(dict, "BANANA")
    dict = {'name': ['neko', 'wanko', 'panda'], 'count': ['99', '999', '1']}
    new_dict = {'name': ['banana'], 'count': ['99']}
    dict.update(new_dict)
    print(dict)
    write_csv(filename, dict)

main()



# name = "Test Name"
#
# with open("restaurants_ranking.csv", "r+") as csv_file:
#     reader = csv.DictReader(csv_file)
#
#     for row in reader:
#         cprint(f"{name}, I recommend {row['name']} restaurant." +
#                f"[♥{row['count']}]"
#                f" Do you like? [y/n]", "cyan", attrs=["bold", "reverse"])
#         cprint("> ", end="")
#
#
#         dic = {"y": True, "yes": True, "n": False, 'no': False}
#         while True:
#             is_liked = dic.get(input("").lower(), -1)
#             if type(is_liked) is bool:
#                 break
#             cprint("Oops, Please input again.", "red")
#             cprint("> ", end="")
#
#         if is_liked:
#             restaurant = row["name"]
#             num = int(row["count"]) + 1
#
#             print(row["name"], row["count"])
#             row.clear()
#             row.update({"name": restaurant, "count": num})
#             print(row["name"], row["count"])
#             writer.writerow(row)
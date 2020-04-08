import csv


def read_csv(filename):

    """
    :param filename:
    :return: dic
    """

    with open(filename, "r") as f:
        reader = csv.DictReader(f, delimiter=",", quotechar='"')
        dic = {}
        for row in reader:
            dic.update({row["name"]: row["count"]})
        return dic


def write_csv(filename, fieldnames, dic):
    """

    :param filename:
    :param fieldnames:
    :param dic:
    :return:
    """
    with open(filename, 'w') as f:

        writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",", quotechar='"')
        writer.writeheader()

        for k, v in dic.items():
            writer.writerow({"name": k, "count": v})


if __name__ == "__main__":

    filename = "restaurants_ranking.csv"
    dic = read_csv(filename)
    print("R", dic)

    newdic = {}
    print("U", newdic)
    dic.update(newdic)

    print("W", dic)
    write_csv(filename, dic)
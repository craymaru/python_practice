from roboter import utils

def main():

    filename = "restaurants_ranking.csv"
    dic = utils.read_csv(filename)
    print("R", dic)

    newdic = {}
    print("U", newdic)
    dic.update(newdic)

    print("W", dic)
    utils.write_csv(filename, dic)

main()
from roboter.csv_rw import read_csv
from roboter.csv_rw import write_csv




if __name__ == "__main__":

    filename = "restaurants_ranking.csv"
    dic = read_csv(filename)
    print("R", dic)

    newdic = {}
    print("U", newdic)
    dic.update(newdic)

    print("W", dic)
    write_csv(filename, dic)
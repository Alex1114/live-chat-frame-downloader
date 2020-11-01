import csv
import pandas as pd
import argparse


def search_keywords(filename, search, output):
    df = pd.read_csv(filename)

    with open(search, 'r') as csvfile:
        search_list = csv.DictReader(csvfile)
        column = [row['keywords'] for row in search_list]

    key = column[0]
    j = 0
    for i,words in enumerate(column):
        if j <= i:
            key = str(key) + "|" + str(column[i])
            j = j + 1

    loc = df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Search keywords in .csv',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('filename', help='.csv filename')

    parser.add_argument("search", help='search .csv name')

    parser.add_argument('output', help='output name')

    args = parser.parse_args()

    search_keywords(args.filename, args.search, args.output)

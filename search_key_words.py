import csv
import pandas as pd
import argparse

def or_1(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    loc=df[df['message'].str.contains(key_1)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def or_2(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key = key_1 + "|" + key_2
    loc=df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def or_3(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key = key_1 + "|" + key_2 + "|" + key_3
    loc=df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def and_2(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    loc=df[df['message'].str.contains(key_1)]
    loc=loc[loc['message'].str.contains(key_2)]    
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def and_3(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    loc=df[df['message'].str.contains(key_1)]
    loc=loc[loc['message'].str.contains(key_2)]
    loc=loc[loc['message'].str.contains(key_3)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Search keywords in .csv',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('filename', help='.csv filename')

    parser.add_argument("mode",type=str,nargs="+")

    parser.add_argument('output', help='output name')
    
    args = parser.parse_args()

    if args.mode[0] == "or":
        print("Search Mode : Or, " + args.mode[1] + " keyword.") 
        if args.mode[1] == "1":
            or_1(args.filename, args.output)
        if args.mode[1] == "2":
            or_2(args.filename, args.output)
        if args.mode[1] == "3":
            or_3(args.filename, args.output)

    if args.mode[0] == "and":
        print("Search Mode : And, " + args.mode[1] + " keyword.") 
        if args.mode[1] == "1":
            or_1(args.filename, args.output)
        if args.mode[1] == "2":
            and_2(args.filename, args.output)
        if args.mode[1] == "3":
            and_3(args.filename, args.output)
        
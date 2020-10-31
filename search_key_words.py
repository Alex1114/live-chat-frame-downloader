import csv
import pandas as pd
import argparse


def or_1(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    loc = df[df['message'].str.contains(key_1)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


def or_2(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key = key_1 + "|" + key_2
    loc = df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


def or_3(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key = key_1 + "|" + key_2 + "|" + key_3
    loc = df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


def or_4(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key = key_1 + "|" + key_2 + "|" + key_3 + "|" + key_4
    loc = df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


def or_5(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key = key_1 + "|" + key_2 + "|" + key_3 + "|" + key_4 + "|" + key_5
    loc = df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


def or_6(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key_6 = input('Sixth keyword : ')
    key = key_1 + "|" + key_2 + "|" + key_3 + "|" + key_4 + "|" + key_5 + "|" + key_6
    loc = df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


def or_7(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key_6 = input('Sixth keyword : ')
    key_7 = input('Seventh keyword : ')
    key = key_1 + "|" + key_2 + "|" + key_3 + "|" + key_4 + "|" + key_5 + "|" + key_6 + "|" + key_7
    loc = df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


def or_8(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key_6 = input('Sixth keyword : ')
    key_7 = input('Seventh keyword : ')
    key_8 = input('Eighth keyword : ')
    key = key_1 + "|" + key_2 + "|" + key_3 + "|" + key_4 + "|" + key_5 + "|" + key_6 + "|" + key_7 + "|" + key_8
    loc = df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


def or_9(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key_6 = input('Sixth keyword : ')
    key_7 = input('Seventh keyword : ')
    key_8 = input('Eighth keyword : ')
    key_9 = input('Ninth keyword : ')
    key = key_1 + "|" + key_2 + "|" + key_3 + "|" + key_4 + "|" + key_5 + "|" + key_6 + "|" + key_7 + "|" + key_8 + "|" + key_9
    loc = df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


def or_10(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key_6 = input('Sixth keyword : ')
    key_7 = input('Seventh keyword : ')
    key_8 = input('Eighth keyword : ')
    key_9 = input('Ninth keyword : ')
    key_10 = input('Tenth keyword : ')
    key = key_1 + "|" + key_2 + "|" + key_3 + "|" + key_4 + "|" + key_5 + "|" + key_6 + "|" + key_7 + "|" + key_8 + "|" + key_9 + "|" + key_10
    loc = df[df['message'].str.contains(key)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

# ===============================================================================================

def and_2(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    loc = df[df['message'].str.contains(key_1)]
    loc = loc[loc['message'].str.contains(key_2)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


def and_3(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    loc = df[df['message'].str.contains(key_1)]
    loc = loc[loc['message'].str.contains(key_2)]
    loc = loc[loc['message'].str.contains(key_3)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def and_4(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    loc = df[df['message'].str.contains(key_1)]
    loc = loc[loc['message'].str.contains(key_2)]
    loc = loc[loc['message'].str.contains(key_3)]
    loc = loc[loc['message'].str.contains(key_4)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def and_5(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    loc = df[df['message'].str.contains(key_1)]
    loc = loc[loc['message'].str.contains(key_2)]
    loc = loc[loc['message'].str.contains(key_3)]
    loc = loc[loc['message'].str.contains(key_4)]
    loc = loc[loc['message'].str.contains(key_5)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def and_6(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key_6 = input('Sixth keyword : ')
    loc = df[df['message'].str.contains(key_1)]
    loc = loc[loc['message'].str.contains(key_2)]
    loc = loc[loc['message'].str.contains(key_3)]
    loc = loc[loc['message'].str.contains(key_4)]
    loc = loc[loc['message'].str.contains(key_5)]
    loc = loc[loc['message'].str.contains(key_6)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def and_7(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key_6 = input('Sixth keyword : ')
    key_7 = input('Seventh keyword : ')
    loc = df[df['message'].str.contains(key_1)]
    loc = loc[loc['message'].str.contains(key_2)]
    loc = loc[loc['message'].str.contains(key_3)]
    loc = loc[loc['message'].str.contains(key_4)]
    loc = loc[loc['message'].str.contains(key_5)]
    loc = loc[loc['message'].str.contains(key_6)]
    loc = loc[loc['message'].str.contains(key_7)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def and_8(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key_6 = input('Sixth keyword : ')
    key_7 = input('Seventh keyword : ')
    key_8 = input('Eighth keyword : ')
    loc = df[df['message'].str.contains(key_1)]
    loc = loc[loc['message'].str.contains(key_2)]
    loc = loc[loc['message'].str.contains(key_3)]
    loc = loc[loc['message'].str.contains(key_4)]
    loc = loc[loc['message'].str.contains(key_5)]
    loc = loc[loc['message'].str.contains(key_6)]
    loc = loc[loc['message'].str.contains(key_7)]
    loc = loc[loc['message'].str.contains(key_8)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def and_9(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key_6 = input('Sixth keyword : ')
    key_7 = input('Seventh keyword : ')
    key_8 = input('Eighth keyword : ')
    key_9 = input('Ninth keyword : ')
    loc = df[df['message'].str.contains(key_1)]
    loc = loc[loc['message'].str.contains(key_2)]
    loc = loc[loc['message'].str.contains(key_3)]
    loc = loc[loc['message'].str.contains(key_4)]
    loc = loc[loc['message'].str.contains(key_5)]
    loc = loc[loc['message'].str.contains(key_6)]
    loc = loc[loc['message'].str.contains(key_7)]
    loc = loc[loc['message'].str.contains(key_8)]
    loc = loc[loc['message'].str.contains(key_9)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")

def and_10(filename, output):
    df = pd.read_csv(filename)
    key_1 = input('First keyword : ')
    key_2 = input('Second keyword : ')
    key_3 = input('Third keyword : ')
    key_4 = input('Fourth keyword : ')
    key_5 = input('Fifth keyword : ')
    key_6 = input('Sixth keyword : ')
    key_7 = input('Seventh keyword : ')
    key_8 = input('Eighth keyword : ')
    key_9 = input('Ninth keyword : ')
    key_10 = input('Tenth keyword : ')
    loc = df[df['message'].str.contains(key_1)]
    loc = loc[loc['message'].str.contains(key_2)]
    loc = loc[loc['message'].str.contains(key_3)]
    loc = loc[loc['message'].str.contains(key_4)]
    loc = loc[loc['message'].str.contains(key_5)]
    loc = loc[loc['message'].str.contains(key_6)]
    loc = loc[loc['message'].str.contains(key_7)]
    loc = loc[loc['message'].str.contains(key_8)]
    loc = loc[loc['message'].str.contains(key_9)]
    loc = loc[loc['message'].str.contains(key_10)]
    loc.to_csv(output, encoding='utf8')
    print("Finish!")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Search keywords in .csv',
        formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument('filename', help='.csv filename')

    parser.add_argument("mode", type=str, nargs="+")

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
        if args.mode[1] == "4":
            or_4(args.filename, args.output)
        if args.mode[1] == "5":
            or_5(args.filename, args.output)
        if args.mode[1] == "6":
            or_6(args.filename, args.output)
        if args.mode[1] == "7":
            or_7(args.filename, args.output)
        if args.mode[1] == "8":
            or_9(args.filename, args.output)
        if args.mode[1] == "9":
            or_9(args.filename, args.output)
        if args.mode[1] == "10":
            or_10(args.filename, args.output)

    if args.mode[0] == "and":
        print("Search Mode : And, " + args.mode[1] + " keyword.")
        if args.mode[1] == "1":
            or_1(args.filename, args.output)
        if args.mode[1] == "2":
            and_2(args.filename, args.output)
        if args.mode[1] == "3":
            and_3(args.filename, args.output)
        if args.mode[1] == "4":
            and_4(args.filename, args.output)
        if args.mode[1] == "5":
            and_5(args.filename, args.output)
        if args.mode[1] == "6":
            and_6(args.filename, args.output)
        if args.mode[1] == "7":
            and_7(args.filename, args.output)
        if args.mode[1] == "8":
            and_8(args.filename, args.output)
        if args.mode[1] == "9":
            and_9(args.filename, args.output)
        if args.mode[1] == "10":
            and_10(args.filename, args.output)

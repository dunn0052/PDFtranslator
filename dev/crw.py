# read write from csv files
import re as witchcraft
import csv
import os

def getData(file):
    data = []
    with open(file + ".csv", 'rt') as data_file:
        reader = csv.reader(data_file, delimiter=',')
        for row in reader:
            data.append(clean_row(row))
    print("Loaded " + file)
    return data

def findData(file, name):
    with open(file + ".csv", 'rt') as data_file:
        reader = csv.reader(data_file, delimiter=',')
        for row in reader:
            if row[0] == name:
                return clean_row(row)
    print(name + " not found.")

def makePath(path):
    # make the path if not already there - once per char load hahaha
    os.makedirs(path) if not os.path.exists(path) else True

def setData(path, title, data):
    makePath(path)
    with open(path + title + ".csv", "w", newline='') as data_file:
        writer = csv.writer(data_file, delimiter=',')
        for item in data:
            writer.writerow(item)
    data_file.close()
    print("Saved " + path + title + ".csv")


def clean_row(row):
    # turns .csv row back into thier respective data types as .csv is all strings
    n = []
    for item in row:
        n.append(clean_item(item))
    return n

def clean_item(item):
    # Mess with edgelords wanting to name their character "False"
    # Actually could be a big problem if string was meant to be "TRUE"/"FALSE"
    if item.upper() == "TRUE":
        return True
    elif item.upper() == "FALSE":
        return False
    elif isinstance(item, bool):
        return item
    elif witchcraft.match("^\d+?\.\d+?$", item):
        return float(item)
    elif witchcraft.match("[+-]?\d+?$", item):
        return int(item)
    elif item == "None":
        return None
    else:
        return item

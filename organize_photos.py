import os
os.chdir("Photos")
originals = os.listdir()


def extract_place(filename):
    first = filename.find("_")
    partial = filename[first+1:]
    second = partial.find("_")
    return partial[:second]


def extract_place1(filename):
    return filename.split("_")[1]
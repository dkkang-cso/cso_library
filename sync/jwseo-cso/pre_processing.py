# -*- coding: utf-8 -*-
def file_open(file):
    f = open(file, 'r')
    lines = f2. readlines()
    #pre_processing
    for line in lines:
        line = rep(line)
        sd.extend(line.split(" "))
    # remove using filter
    sd = list(filter(None, sd))


def rep(str):
    char = ["\n", "\t"]
    str2 =str
    for i in char:
        str2 = str2.replace(i,"")
    return str2

def fnd(arr, idx):
    res_list = [i for i, value in enumerate(arr) if value == "ifdef"]
    num1 = res_list[idx]
    return num1

def elsenum0(arr): # 첫번째 else위치
    res_list = [i for i, value in enumerate(arr) if value == "else"]
    num2 = res_list[0]
    return num2

def elsenum1(arr): # 두번째 else위치
    res_list = [i for i, value in enumerate(arr) if value == "else"]
    res_list1 = [i for i, value in enumerate(arr) if value == "endif"]
    if len(res_list) > 1:
        num3 = res_list[1]
    else:
        num3 = res_list1[0]
    return num3




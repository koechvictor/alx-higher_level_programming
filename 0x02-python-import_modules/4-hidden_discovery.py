#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    list = []
    for i in dir(hidden_4):
        if i[0] != '_':
            list.append(i)
    for i in list:
        print(i)

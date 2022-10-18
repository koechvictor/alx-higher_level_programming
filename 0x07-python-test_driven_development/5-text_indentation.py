#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after each '.', '?', ':'
"""
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    newText = ""
    for i in range(len(text)):
        if not i == 0 and text[i] == " " and text[i - 1] in ".?:":
            continue
        newText += text[i]
        if text[i] in ".?:":
            newText += "\n\n"
    print(newText, end="")

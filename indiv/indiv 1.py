#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def split(text):
    vowels = 'ueioay'
    for word in text:
        words = []
        for prword in vowels:
            if word[0] == prword:
                words = str(vowels)
        for prword in words:
            if word.endswith(prword):
                print(word)


if __name__ == "__main__":
    with open("text1.txt", "r", encoding="utf-8") as fileptr:
        sentences = fileptr.readlines()
    text1 = str(sentences).lower().split()
    print(split(text1))
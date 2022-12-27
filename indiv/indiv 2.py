#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == "__main__":

    with open("oc.txt", "w") as fileptr:
        slovar = {'5': 'A', '4': 'B', '3': 'C', '2': 'D', '1': 'F'}
        while True:
            i = input()

            ii = {value: key for key, value in slovar.items()}
            if i in slovar.keys():
                fileptr.write(f'{i} = {slovar[i]}\n')
                print(f'{i} = {slovar[i]}')
            elif i in ii.keys():
                fileptr.write(f'{i} = {ii[i]}\n')
                print(f'{i} = {ii[i]}')
            elif i == '':
                break
            else:
                fileptr.write(f'{i} = Данное значение является недопустимым\n')
                print(f'{i} = Данное значение является недопустимым')
        print(fileptr)
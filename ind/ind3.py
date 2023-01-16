#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

"""
Если передается 3> параметров, то выдается ошибка.
Если меньше 3, то слишком мало.
Если 1-й параметр не начинается с --n или --name, то выводится ошибка.
Если все условия выполнены, то выводится приветствие
"""

import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Привет, мир!")
    else:
        if len(sys.argv) < 3:
            print("Ошибка. Слишком мало параметров.")
            sys.exit(1)

        if len(sys.argv) > 3:
            print("Ошибка. Слишком много параметров.")
            sys.exit(1)

        param_name = sys.argv[1]
        param_value = sys.argv[2]

        if (param_name == "--name" or
                param_name == "-n"):
            print("Привет, {}!".format(param_value))
        else:
            print("Ошибка. Неизвестный параметр '{}'".format(param_name))
            sys.exit(1)

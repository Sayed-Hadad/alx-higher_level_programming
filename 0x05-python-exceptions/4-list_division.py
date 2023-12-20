#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    res_list = []

    for i in range(list_length):
        res = 0

        try:
            element_1 = my_list_1[i] if i < len(my_list_1) else 0
            element_2 = my_list_2[i] if i < len(my_list_2) else 0

            res = element_1 / element_2
        except ZeroDivisionError:
            print("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        finally:
            res_list.append(res)

    return res_list

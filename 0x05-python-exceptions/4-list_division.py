#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    divi_list = []
    for idx in range(0, list_length):
        try:
            value = my_list_1[idx] / my_list_2[idx]
        except TypeError:
            value = 0
            print("wrong type")
            pass
        except ZeroDivisionError:
            value = 0
            print("division by 0")
            pass
        except IndexError:
            value = 0
            print("out of range")
            pass
        finally:
            divi_list.append(value)
    return divi_list

#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenght):
    newlist = []
    for i in range(list_lenght):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print('Division by 0')
            result = 0
        except TypeError:
            print('Wrong type')
            result = 0
        except IndexError:
            print('Out of range')
        finally:
            newlist.append(result)

    return (newlist)

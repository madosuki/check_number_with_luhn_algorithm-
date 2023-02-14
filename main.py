import sys

def get_number_list_from_string(s):
    listed = list(s)
    number_list = list(map(lambda x: int(x), listed))

    return number_list

def split_digit(x):
   s = str(x) 
   num_list = get_number_list_from_string(s)
   
   return num_list


def check_validate(l):
    l.reverse()
    length = len(l)
    check_digit = l[0]
    tmp = list(map(lambda x: x[1] * 2 if (x[0] + 1) % 2 == 0 else x[1], enumerate(l)))
    
    result = []
    for i in tmp:
        if i > 9:
            n_list = split_digit(i)
            for j in n_list:
                result.append(j)
        else:
            result.append(i)
    
    sumed = sum(result)
    return (sumed % 10) == 0

def main():
    args = sys.argv
    if len(args) < 2:
        print("require 1 argument")
        return

    target = args[1]
    number_list = get_number_list_from_string(target)
    print("{0} is {1}".format(target, check_validate(number_list)))
    
main()


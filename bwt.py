
def print_list(lista):
    for i in range(len(lista)):
        print(lista[i])
    print()


def create_bwt_list(bwt_string):
    new_string = bwt_string + "$"
    bwt_list = [new_string]

    for i in range(len(bwt_string)):
        new_string = new_string[1:] + new_string[0]
        bwt_list.append(new_string)

    return bwt_list


def sort_list(bwt_list):
    bwt_list.sort()
    return bwt_list


def get_bwt(bwt_list):
    output = ""

    for i in range(len(bwt_list)):
        output += bwt_list[i][-1]

    return output


def main(messaggio):
    

    a_list = create_bwt_list(messaggio)

    print("Rotazioni:")
    print_list(a_list)

    a_list = sort_list(a_list)

    print("Rotazioni ordinate:")
    print_list(a_list)

    bwt = get_bwt(a_list)

    print("Burrows Wheeler Transform:", bwt)



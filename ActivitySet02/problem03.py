

def get_cs():
    str = input("Enter string: ")


def cs_to_lot(cs):
    cs = cs.split( )
    return cs


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()

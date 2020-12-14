from lord_of_the_rings.mortal_men_rings import the_nine
from lord_of_the_rings.dwarf_rings import the_seven
from lord_of_the_rings.elven_rings import the_three


def rule_them_all():
    return the_nine.rule() and the_seven.rule() and the_three.rule()


def find_them():
    return the_nine.find() and the_seven.find() and the_three.find()


def bring_them_all_and_in_the_darkness_bind_them():
    print("Method not supported yet.")
    raise Exception


if __name__ == '__main__':
    rule_them_all()
    find_them()
    bring_them_all_and_in_the_darkness_bind_them()

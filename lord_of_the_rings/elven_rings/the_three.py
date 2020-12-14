from lord_of_the_rings.elven_rings import narya, neya, vilya


def find():
    return narya.find() and neya.find() and vilya.find()


def rule():
    return narya.rule() and neya.rule() and vilya.rule()


if __name__ == '__main__':
    find()
    rule()

# ab(a|b)*a(a|b)?
def q0(znak):
    return 1 if znak == "0" else 0


def q1(znak):
    return 2 if znak == "1" else 0

def q2(znak1, znak2):
    if znak1 == "0":
        return 3
    else:
        return 0


def sprawdz(ciag):
    stan = "start"
    if len(ciag) < 3:
        return "N"
    for i in ciag:
        if i != "0" and i != "1":
            return "N"

    for i in range(len(ciag)):
        if stan == 0:
            stan = 'N'
        elif stan == "start":
            stan = q0(ciag[i])
            continue
        elif stan == 1:
            stan = q1(ciag[i])
            continue
        elif stan == 2:
            if ciag[-2] == "0":
                stan = 3
                break
            elif ciag[-1] == "0":
                stan = 3
                break
            else:
                stan = 0
                break
        else:
            stan = 0
    if stan == 3:
        return 'A'
    else:
        return 'N'


if __name__ == "__main__":
    print("Wpisz ciag znakow: ")
    ciag = input()
    print("Ciag: " + ciag)
    print("Wynik: " + sprawdz(ciag))

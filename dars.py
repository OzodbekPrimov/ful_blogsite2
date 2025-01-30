# def salom_ber(son,son2):
#     # print(son+son2)  # output:
#     return son+son2 # return value
#
# salom_ber(6,7)
# print(f)
# salom_ber()
# salom_ber()

def hisobla(son):
    if son < 100:
        return "Kichik son"
    else:
        return "Katta son"


# print(hisobla(230))

# def tanishtir(ism,familya,yosh):
#     return f"""
#     Salom, Mening ismim {ism}. Familyam {familya}.
#     Yoshim esa {yosh}
#     """
# print(tanishtir("John", "Doe", 24))

def hudud(mylist):
    for i in mylist:
        print(i + "liklar")


hudud(["Toshkent", "Buxoro", "Namangan"])


def person(ism, familya):
    if familya[-2:] == "va":
        print("woman")
    else:
        print("Man")
person("Akmal", "Tohirova")

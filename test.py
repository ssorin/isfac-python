def hello():
    print("hello world !!")


# if __name__ == '__main__':
#     hello()


prenom = input("Bonjour, quel est ton prenom ?")

print("Bonjour et bienvenue %s " % prenom)
print("Bonjour et bienvenue " + prenom)
print("Bonjour et bienvenue", prenom)
print(f"Bonjour et bienvenue {prenom}")
print("Bonjour et bienvenue {0}".format(prenom))
print("Bonjour et bienvenue {name}".format(name=prenom))

table_multiplication = int(input("on multiplie quoi ?"))


print(f"1 x {table_multiplication} =", table_multiplication * 1)
print(f"2 x {table_multiplication} = %s" % (table_multiplication * 2))
print(f"3 x {table_multiplication} =", table_multiplication * 3)
print(f"4 x {table_multiplication} =", table_multiplication * 4)
print(f"5 x {table_multiplication} =", table_multiplication * 5)
print(f"6 x {table_multiplication} =", table_multiplication * 6)
print(f"7 x {table_multiplication} =", table_multiplication * 7)
print(f"8 x {table_multiplication} =", table_multiplication * 8)
print(f"9 x {table_multiplication} =", table_multiplication * 9)
# print(f"9 x " + str(table_multiplication) + " =", table_multiplication * 10)
#
# multipli_1 = f"1 x {table_multiplication} =", table_multiplication * 1
# multipli_1a = "1 x " + str(table_multiplication) + " =", table_multiplication * 1
# multipli_1a = "1 x %s = %s" % (table_multiplication, table_multiplication * 1)


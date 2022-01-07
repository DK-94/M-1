my_l = [1,2,3]

print(my_l)

for adada in range(4,10,1):
    my_l.append(adada)
print(my_l)

l_2 = ["ad","da", "ab", "ba"]

my_l.extend(l_2)
print(my_l)
z = len(my_l)
# for az in range(0,z,2):
#     print(my_l[az])

i = 0
while i < z:
    print(my_l[i])
    i = i+2


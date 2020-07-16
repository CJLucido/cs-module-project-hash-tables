# Your code here
# import sys
# sys.path.insert(0, '/Users/cjose/Documents/Python/Lambda/cs-module-project-hash-tables/hashtable/hashtable.py')
# # cs_module_project_hashtables = __import__('cs-module-project-hashtables')
# # sys.path.append('.')
from hashtable import HashTable, HashTableEntry

# zTable = HashTable(2401)

# yTable = HashTable(404)

# xTable = HashTable(153)


# for i in range(0, 2400):
#     zTable.put(str(i), " ")
# for i in range(0, 403):
#     yTable.put(str(i), zTable)
# for i in range(-3, 149):
#     xTable.put(str(i), yTable)

# def expensive_seq(x, y, z):
#     # Your code here
#     # zTable = HashTable(2401)

#     # yTable = HashTable(404)

#     # xTable = HashTable(153)


#     # for i in range(0, 2400):
#     #     zTable.put(str(i), " ")
#     # for i in range(0, 403):
#     #     yTable.put(str(i), zTable)
#     # for i in range(-3, 149):
#     #     xTable.put(str(i), yTable)

#     int(x)
#     int(y)
#     int(z)
#     if "-" or "0" in x:
#         # print(y)
#         # print((zTable.get(str(z))).value)
#         # print(xTable.get(str(x-1)).get(str(y+1)).__dir__())
#         new_y = xTable.get(str(x))
#         print("newy", new_y.__dir__())
#         new_z = new_y.get(str(y))
#         print("newz", new_z)
#         new_z.put(str(z), (int(y) + int(z)))
#         return new_z.get(str(z))
#         # return xTable.get(str(x-1)).get(str(y+1)).put(str(z), (int(y) + int(z)))
#     else:
#         int(x)
#         int(y)
#         int(z)
#         # print(y)
#         # print(type(y))
#         dir(zTable.get(str(z)))
#         new_y = xTable.get(str(x-1))
#         new_y2 = xTable.get(str(x-2))
#         new_y3 = xTable.get(str(x-3))

#         new_z = new_y.get(str(y+1))
#         new_z2 = new_y2.get(str(y+2))
#         new_z3 = new_y3.get(str(y+3))

#         zValue = new_z(str(z))
#         zValue2 = new_z2(str(z*2))
#         zValue3 = new_z3(str(z*3))
#         return zValue + zValue2 + zValue3
#         # return xTable.get(str(x-1)).get(str(y+1)).get(str(z)) + xTable.get(str(x-2)).get(str(y+2)).get(str(z*2)) + xTable.get(str(x-3)).get(str(y+3)).get(str(z*3))

#         # return xTable.get(str(x-1)).get(str(y+1)).put(str(z), expensive_seq(str(x-1),str(y+1),str(z))) + xTable.get(str(x-2)).get(str(y+2)).put(expensive_seq(str(x-2),str(y+2),str(z*2))) + xTable.get(str(x-3)).get(str(y+3)).put(expensive_seq(str(x-3),str(y+3),str(z*3)))

#     # if x <= 0: y + z
#     # if x >  0: expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)

#     # make an x-1 table, x-2 table, x-3 table (x key, y-table[ykey])
#     # in each have a y+1 table, y+2, and y+3 (y key, z-table[zkey])

# zTable = HashTable(148949800)

xyTable = []

# xTable = HashTable(153)


# for i in range(0, 148949800):
#     zTable.put(str(i), " ")

# for i in range(-3, 150):
#     for k in range(0, 404):
#         xyTable.append((str(i), str(k)))
# print(xyTable)
# zTable = HashTable(148949800) NEVER DO
zTable = {}
for i in range(-3, 150):
        for k in range(0, 404):
            xyTable.append((str(i), str(k)))
    # print(xyTable)

yTable = HashTable(len(xyTable))
for i in xyTable:
        yTable.put(str(i), "")
        
def expensive_seq(x, y, z):
    # Your code here
    yTable.put(str((x, y)), zTable)
    # ourZ = yTable.get(str((x, y)))
    
    if x <= 0:
        # ourZ.put(str(z), (int(y) + int(z)))
        # print(ourZ.get(str(z)))
        # print("len", len(ourZ.capacity))
        # return ourZ.get(str(z))
        if zTable.get(str((str(x), str(y),str(z)))):
            pass
        else: 
            zTable[str((str(x), str(y),str(z)))] = (int(y) + int(z))

        # print("ourZ", str((str(x), str(y),str(z))))
        # print("ourZ", zTable[str((str(x), str(y),str(z)))])
        # print("ourZ", zTable)
        # print("ourZ", len(zTable))
        return zTable[str((str(x), str(y),str(z)))]
    else:
        print("newx", x)
        zValue1 = expensive_seq(x-1,y+1,z)
        zValue2 = expensive_seq(x-2,y+2,z*2)
        zValue3 = expensive_seq(x-3,y+3,z*3)
        if zTable.get(str((str(x-1), str(y+1),str(z)))):
            zValue1 = zTable[str((str(x-1), str(y+1),str(z)))]
            # print("woohoo")
        if zTable.get(str((str(x-2), str(y+2),str(z*2)))):
            zValue2 = zTable[str((str(x-2), str(y+2),str(z*2)))]
            # print("woohoo2")
        if zTable.get(str((str(x-3), str(y+3),str(z*3)))):
            zValue3 = zTable[str((str(x-3), str(y+3),str(z*3)))]
            # print("woohoo3")
        print(zValue1 + zValue2 + zValue3)
        zTable[str((str(x), str(y),str(z)))] = zValue1 + zValue2 + zValue3
        return zValue1 + zValue2 + zValue3
        # return expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
    # if x <= 0: y + z
    # if x >  0: expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)

    # make an x-1 table, x-2 table, x-3 table (x key, y-table[ykey])
    # in each have a y+1 table, y+2, and y+3 (y key, z-table[zkey])

# print(expensive_seq(2, 3, 4))

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

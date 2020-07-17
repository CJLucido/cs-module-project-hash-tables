# Your code here
# import sys
# sys.path.insert(0, '/Users/cjose/Documents/Python/Lambda/cs-module-project-hash-tables/hashtable/hashtable.py')
# # cs_module_project_hashtables = __import__('cs-module-project-hashtables')
# # sys.path.append('.')
from hashtable import HashTable, HashTableEntry

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
    
    if x <= 0:
        if zTable.get(str((x, y,z))):
            pass
        else: 
            zTable[(str((x, y,z)))] = (int(y) + int(z))
        return zTable[(str((x, y,z)))]
    else:
        zValue1 = ""
        zValue2 = ""
        zValue3 = ""
        if zTable.get((str((x, y,z)))):
            return zTable[(str((x, y,z)))]
        else:
            if zTable.get(str(((x-1), (y+1),(z)))):
                zValue1 = zTable[str(((x-1), (y+1),(z)))]
            else:
                zValue1 = expensive_seq(x-1,y+1,z)
                # print("woohoo")
            if zTable.get(str(((x-2), (y+2),(z*2)))):
                zValue2 = zTable[str(((x-2), (y+2),(z*2)))]
            else:
                zValue2 = expensive_seq(x-2,y+2,z*2)
                # print("woohoo2")
            if zTable.get(str(((x-3), (y+3),(z*3)))):
                zValue3 = zTable[str(((x-3), (y+3),(z*3)))]
            else:
                zValue3 = expensive_seq(x-3,y+3,z*3)
                # print("woohoo3")
            # print(zValue1 + zValue2 + zValue3)
            zTable[(str((x, y,z)))] = zValue1 + zValue2 + zValue3
            return zValue1 + zValue2 + zValue3

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

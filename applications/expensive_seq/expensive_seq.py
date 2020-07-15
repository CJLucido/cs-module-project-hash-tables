# Your code here
# import sys
# sys.path.insert(0, '/Users/cjose/Documents/Python/Lambda/cs-module-project-hash-tables/hashtable/hashtable.py')
# # cs_module_project_hashtables = __import__('cs-module-project-hashtables')
# # sys.path.append('.')
from hashtable import HashTable, HashTableEntry

zTable = HashTable(2401)

yTable = HashTable(404)

xTable = HashTable(153)


for i in range(0, 2400):
    zTable.put(str(i), " ")
for i in range(0, 403):
    yTable.put(str(i), zTable)
for i in range(-3, 149):
    xTable.put(str(i), yTable)

def expensive_seq(x, y, z):
    # Your code here
    if x <= 0:
        xTable.get(str(x-1)).get(str(y+1)).get(str(z)).put(y + z)

    if x >  0:
        xTable.get(str(x-1)).get(str(y+1)).put(expensive_seq(x-1,y+1,z))
        xTable.get(x-2).get(y+2).put(expensive_seq(x-2,y+2,z*2))
        xTable.get(x-3).get(y+3).put(expensive_seq(x-3,y+3,z*3))

    # if x <= 0: y + z
    # if x >  0: expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)

    # make an x-1 table, x-2 table, x-3 table (x key, y-table[ykey])
    # in each have a y+1 table, y+2, and y+3 (y key, z-table[zkey])


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))

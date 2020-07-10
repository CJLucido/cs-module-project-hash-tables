class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8

class LinkedList:
    def __init__(self):
        self.head = None
    
    def find_by_key(self, key):
        current = self.head

        while current is not None:
            if current.key == key:
                # print("here")
                return current
            current = current.next
    
    # def find_by_value(self, value):
    #     current = self.head

    #     while current is not None:
    #         if current.value.value == value:
    #             return current
    #         current.next

    def insert_at_tail(self, key, value):
        node = HashTableEntry(key, value)

        if self.head is None:
            self.head = node
        else:
            current = self.head
            print("adding to tail")
            while current.next is not None:
                current = current.next
            current.next = node

    def delete(self, key):
        current = self.head

        if current is None:
            return None

        if current.key == key:
            self.head = current.next
            return current #it will just be garbage collected eventually (repointing to next in line)

        else:
            previous = current
            current = current.next

            while current is not None:
                if current.key == key: # found it
                    previous.next = current.next
                    return current #what was deleted
                
                else:
                    previous = current
                    current = current.next
            
            return None

class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        # LL = LinkedList()
        self.capacity = []
        for _ in range(0, capacity):
            self.capacity.append(LinkedList())
        self.capacity_entered = capacity
        # self.delete_counter = 0
        # print(self.capacity)

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.capacity)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        
        hash_offset_basis = 14695981039346656037
        hash = hash_offset_basis
        fnv_prime = 1099511628211
        # for byte in key:
        hash = hash * fnv_prime
        # print(int.from_bytes(bytes(key, 'utf-8'), 'little'))
         # for byte in key:
        hash = hash ^ int.from_bytes(bytes(key, 'utf-8'), 'big')
            # hash = bytes(map(operator.xor, hash.to_bytes(14, 'big'),byte.encode('utf-8')))
        # print(hash)

        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381

        for char in key:
            hash = ((hash << 5) + hash) + ord(char)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # print(self.fnv1(key) % len(self.capacity))
        return self.fnv1(key) % self.capacity_entered
        #return self.djb2(key) % self.capacity

    # def hash_index2(self, key):
    #     """
    #     Take an arbitrary key and return a valid integer index
    #     between within the storage capacity of the hash table.
    #     """
    #     # print(self.fnv1(key) % len(self.capacity))
    #     return self.fnv1(key) % len(self.capacity)
    #     #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        new_key = self.hash_index(key)
        
        if self.capacity[new_key] != None:
            print("warning about to overwrite with PUT")

        #self.capacity[new_key] = value # without linked list this is fine


        #find the LL by the key
        chain_in_arr = self.capacity[new_key]
        # print(chain_in_arr)
        #see if the LL has the original key (pre hash)
        if chain_in_arr.find_by_key(key) != None:
             print("That key already exists!")
             if chain_in_arr.find_by_key(key).value == value:
                 print("That key AND value pair already exists!")
             else:
                 chain_in_arr.find_by_key(key).value = value
        else:
            chain_in_arr.insert_at_tail(key, value)
        # print("successful put", self.capacity)



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        new_key = self.hash_index(key)
        #pre LL
        # if len(self.capacity) - 1 >= new_key:
        #      self.capacity[new_key]= None
        #     print("new array", self.capacity)
        # else:
        #     print("Warning")
        
        #find the LL by the key
        chain_in_arr = self.capacity[new_key]
        #see if the LL has the original key (pre hash)
        if chain_in_arr.find_by_key(key) == None:
             print("That key value pair doesn't exist!")
        else:
            chain_in_arr.delete(key)
        print("successful delete")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        new_key = self.hash_index(key)
        # pre LL
        # if len(self.capacity) - 1 >= new_key:
        #     return self.capacity[new_key]
        # else:
        #     return None
        chain_in_arr = self.capacity[new_key]
        #see if the LL has the original key (pre hash)
        if chain_in_arr.find_by_key(key) != None:
             print("Found", chain_in_arr.find_by_key(key))
             return chain_in_arr.find_by_key(key).value
        else:
            print("Couldn't find the droid you're looking for, even combed the desert")
        print("successful get")

        

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
 !!!UNDONE-->       rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        replacement = []
        
        if new_capacity >= self.capacity_entered:
          addToList = [None] * (new_capacity - self.capacity_entered)
        
          for i in addToList:
            self.capacity.append(i)
# REHASHING 
        #   for i in range(1, len(self.capacity)):
        #     value = self.get(f"line_{i}")

        #    # print("value", value)

        #     self.put(f"line_{i}", value)
          replacement = self.capacity
          return replacement
        else:
          replacement = self.capacity[:new_capacity]
          #REHASHING
        #   for i in range(1, len(self.capacity)):
        #     value = self.get(f"line_{i}")
        #     self.put(f"line_{i}", value)
          return replacement

        self.capacity = replacement



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity_entered * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
        # #  print("length of array", len(ht.capacity))

    print("")

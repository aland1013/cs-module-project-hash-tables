class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def find(self, key):
        curr = self.head
        while curr != None:
            if curr.key == key:
                return curr
            else:
                curr = curr.next
        return None
    
    def delete(self, key):
        curr = self.head
        prev = None
        
        if curr.key == key:
            self.head = curr.next
            curr.next = None
            return curr
        
        while curr != None:
            if curr.key == key:
                prev.next = curr.next
                curr.next = None
                return curr
            else:
                prev = curr
                curr = curr.next
        
    def insert_at_head(self, node):
        node.next = self.head
        self.head = node
    
    def insert_at_head_or_overwrite(self, node):
        existingNode = self.find(node.key)
        if existingNode:
            existingNode.key = node.key
            existingNode.value = node.value
        else:
            self.insert_at_head(node)

# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.table = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        occupied_slots = 0
        for i in range(self.capacity):
            if self.table[i]:
                occupied_slots += 1
        
        return occupied_slots / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        fnv_prime = 2**40 + 2**8 + int('0xb3', 16)
        hash = 14695981039346656037 # 64 bit offset basis
        key_bytes = key.encode()
        
        for b in key_bytes:
            hash = hash * fnv_prime
            hash = hash ^ b
            
        return hash
        

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hash = 5381
        
        for char in key:
            hash = 33 * hash ^ ord(char)
        
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        newNode = HashTableEntry(key, value)
        i = self.hash_index(key)
        if not self.table[i]:
            self.table[i] = LinkedList()
        self.table[i].insert_at_head_or_overwrite(newNode)
        
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)
        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        ll = self.table[i]
        deletedNode = ll.delete(key)
        if not deletedNode:
            print(f'{key} not found')

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        i = self.hash_index(key)
        ll = self.table[i]
        node = ll.find(key)
        
        return node.value if node else None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        newTable = HashTable(new_capacity)
        for slot in self.table:
            if slot:
                curr = slot.head
                while curr:
                    newTable.put(curr.key, curr.value)
                    curr = curr.next
        
        self.capacity = new_capacity
        self.table = newTable.table
                


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
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")

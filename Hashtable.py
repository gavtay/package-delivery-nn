# HashTable class using chaining.
# Source: WGU Sources, Getting Greedy, Who Moved My Data
# https://srm--c.vf.force.com/apex/CourseArticle?id=kA03x000000e1g4CAA&groupId=&searchTerm=&courseCode=C950&rtn=/apex/CommonsExpandedSearch
class CreateHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=20):
        self.list = []
        for i in range(initial_capacity):
            self.list.append([])

    # Inserts a new item into the hash table
    # Citing source: WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:  # O(N) CPU time
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Lookup items in hash table
    def lookup(self, key):
        bucket = hash(key) % len(self.list)
        bucket_list = self.list[bucket]
        for pair in bucket_list:
            if key == pair[0]:
                return pair[1]
        return None

    # function to remove item
    def hash_remove(self, key):
        slot = hash(key) % len(self.list)
        destination = self.list[slot]

        # If the key is found in the hash table then remove the item
        if key in destination:
            destination.remove(key)
#Your personal Hash map
class hash_table:
    def __init__(self):
        self.table = [0 for _ in range(26)]

    def hash_function(self, name):
        table_size = 26
        sum = 0
        for i in name:
            sum += ord(i)
        return sum % table_size
    
    def hash_put(self, name, num):
        key = self.hash_function(name)
        self.table[key] = num

    def hash_search(self, name):
        key = self.hash_function(name)
        return self.table[key]

hash_table1 = hash_table()
hash_table1.hash_put('hihi',10)
print(hash_table1.hash_search('hihi'))

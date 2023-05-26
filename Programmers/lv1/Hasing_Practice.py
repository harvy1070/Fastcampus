class Hashtable:

    def __init__(self):
        self.table_length = 139
        self.table = [None for _ in range(self.table_length)]

    def simple_hash(self, name):
        ord_sum = 0
        for letter in name:
            ord_sum += ord(letter)
        return ord_sum % self.table_length

    def put(self, name, num):
        self.table[self.simple_hash(name)] = num

    def show(self):
        for idx, value in enumerate(self.table):
            if value:
                print(idx, value)

    def find(self, name):
        return self.table[self.simple_hash(name)]

boo = Hashtable()
boo.put('Kim', 7458)
boo.put('John', 8569)
boo.put('Smith', 1452)
boo.put('Michael', 2563)

print(boo.find('Kim'))
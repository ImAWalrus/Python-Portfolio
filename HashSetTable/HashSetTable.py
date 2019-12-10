

class HashSetTbl:

    def __init__(self):
        """ constructor creates a 10 empty buckets
        each bucket contains zero or more unique values.
        def. This class maintains a set property (all unique values)
        """
        self.bucket_list = [ [] for i in range(10)]

    def __getitem__(self, v):
        """override retrieval to support syntax: tblobject['red']
        should return the value v in table
        if v not found in table, raise KeyError
        Must use the hash value of v THEN sequential search of bucket
        at index[h(v)]
        """
        h = self.hash_func(v)
        for j in self.bucket_list[h]:
            if v == j:
                return j
        raise KeyError



    def insert(self, v):
        """assignment to support syntax: tblobject.add('blue')
        should add the value v to proper bucket in table IF it does
        not already exist.
        """
        #h = self.hash_func(v)
        for i in range(10):
            for j in self.bucket_list[i]:
                if v == j:
                    pass
                else:
                    self.bucket_list[j].append(v)


    def __iter__(self):
        """ implement generator to allow looping over entire contents
        of the set.
        """
        for i in range(10):
            for j in self.bucket_list[i]:
                yield j

    def __len__(self):
        """ returns the total number of assigned values in table."""
        count = 0
        for i in range(10):
            for j in self.bucket_list[i]:
                count = count + 1
        return count

    def bucket_dump(self):
        """ prints a snapshot of the bucket list to the screen. Example:
            [0]: 'a', 'tree', 'mouse'
            [1]: 'red'
            ...
            [9]: 'top', 'bottom'
        """
        for i in range(10):
            print i
            for j in self.bucket_list[i]:
                print j


    def hash_func(self, v):
        """
        a. computes a hash code for v using python hash() function
        b. compresses hash code relative to size of bucket list.
        returns the compression value
        """
        return hash(v) % 10


if __name__ == '__main__':

    h = HashSetTbl()
    tmp = 'As she said this she looked down at her hands and was surprised to see that she had put on one of the Rabbis little white kid gloves while she was talking How can I have done that she thought I must be growing small again She got up and went to the table to measure herself by it and found that as nearly as she could guess she was now about two feet high and was going on shrinking rapidly she soon found out that the cause of this was the fan she was holding and she dropped it hastily just in time to avoid shrinking away altogether'
    alist = tmp.split()
    h.insert(alist)
    for i in h:
        print i,

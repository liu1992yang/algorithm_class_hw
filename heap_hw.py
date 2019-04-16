class MinHeap:
    def __init__(self):
        self.heaplist = []

    def insert(self, k):
        """
        insert k into minheap
        """
        self.heaplist.append(k)
        i = len(self.heaplist)-1
        while i > 0:
            parent_idx = (i-1)//2
            # if value at index i < its parent, swap
            if self.heaplist[i] < self.heaplist[parent_idx]:
                tmp = self.heaplist[parent_idx]
                self.heaplist[parent_idx] = self.heaplist[i]
                self.heaplist[i] = tmp 
            #go to its parent no matter what
                i = parent_idx
            else:
                break
        return
    
    
        
    def del_min(self):
        """
        delete min of the min heap
        """
        extracted_min = self.heaplist[0]
        self.heaplist[0] = self.heaplist[-1]
        self.heaplist.pop()
        i = 0
        length = len(self.heaplist)
        while i < length//2:
            l_idx = 2*i + 1
            r_idx = 2*i + 2
            if r_idx > length-1:
                if self.heaplist[i] > self.heaplist[l_idx]:
                    temp = self.heaplist[l_idx]
                    self.heaplist[l_idx] = self.heaplist[i]
                    self.heaplist[i] = temp
                    i = l_idx
                else:
                    break
            else:
                if (self.heaplist[i] <= self.heaplist[l_idx]) and (self.heaplist[i]<= self.heaplist[r_idx]):
                    break
                
                else:
                    if self.heaplist[l_idx] == self.heaplist[r_idx]:
                        min_idx = r_idx
                        val = self.heaplist[r_idx]
                    else: 
                        to_swap = {l_idx: self.heaplist[l_idx], r_idx:self.heaplist[r_idx]} 
                        min_idx, val = min(to_swap.items(), key = lambda x:x[1])
                    self.heaplist[min_idx] = self.heaplist[i]
                    self.heaplist[i] = val
                    i = min_idx
                
        return extracted_min

        
class MaxHeap:
    def __init__(self):
        self.heaplist = []
    
    def insert(self, k):
        self.heaplist.append(k)
        i = len(self.heaplist)-1
        while i > 0:
            parent_idx = (i-1)//2
            # if value at index i > its parent, swap
            if self.heaplist[i] > self.heaplist[parent_idx]:
                tmp = self.heaplist[parent_idx]
                self.heaplist[parent_idx] = self.heaplist[i]
                self.heaplist[i] = tmp 
            #go to its parent no matter what
                i = parent_idx
            else:
                break
        return
    
    def del_max(self):
        """
        delete max of the max heap
        """
        extracted_max = self.heaplist[0]
        self.heaplist[0] = self.heaplist[-1]
        self.heaplist.pop()
        i = 0
        length = len(self.heaplist)
        while i < length//2:
            l_idx = 2*i + 1
            r_idx = 2*i + 2
            if r_idx > length-1:
                if self.heaplist[i] < self.heaplist[l_idx]:
                    temp = self.heaplist[l_idx]
                    self.heaplist[l_idx] = self.heaplist[i]
                    self.heaplist[i] = temp
                    i = l_idx
                else:
                    break
            else:
                if (self.heaplist[i] >= self.heaplist[l_idx]) and (self.heaplist[i]>= self.heaplist[r_idx]):
                    break
                
                else:
                    if self.heaplist[l_idx] == self.heaplist[r_idx]:
                        max_idx = r_idx
                        val = self.heaplist[r_idx]
                    else: 
                        to_swap = {l_idx: self.heaplist[l_idx], r_idx:self.heaplist[r_idx]} 
                        max_idx, val = max(to_swap.items(), key = lambda x:x[1])
                    self.heaplist[max_idx] = self.heaplist[i]
                    self.heaplist[i] = val
                    i = max_idx
                
        return extracted_max

def init_partition(min_heap, max_heap, k):
    """
    partition k into two heaps
    """
    if not max_heap.heaplist:
        max_heap.insert(k)
    else:
        if k >= max_heap.heaplist[0]:
            min_heap.insert(k)
        else:
            max_heap.insert(k)
    return
    
def partition_even(min_heap, max_heap):
    while True:
        if len(max_heap.heaplist)-len(min_heap.heaplist) >1:
            extracted = max_heap.del_max()
            min_heap.insert(extracted)
        elif len(min_heap.heaplist)-len(max_heap.heaplist) >1:
            extracted = min_heap.del_min()
            max_heap.insert(extracted)
        else:
            break
    return

def get_median(min_heap, max_heap, length):
    if length%2 == 0:
        return max_heap.heaplist[0]
    else:
        return max(min_heap.heaplist, max_heap.heaplist, key = len)[0]
        
if __name__ == "__main__":
    maxheap = MaxHeap()    
    minheap = MinHeap()
    sum_median = 0
    with open('Median.txt', 'r') as fin:
        counter = 1
        while counter <= 10000: 
            val = int(fin.readline())
            #print(val)
            init_partition(minheap, maxheap, val)
            partition_even(minheap, maxheap)
            #print(minheap.heaplist, maxheap.heaplist)
            sum_median+=get_median(minheap, maxheap, counter)
            counter+=1
    print(sum_median)
    print(sum_median%10000)
    

    

    
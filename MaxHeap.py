class MaxHeap:
    def __init__(self):
        self.heap = []

    def get_parent(self,i):
        return int((i-1)/2)
    def get_leftchild(self,i):
        return 2*i+1
    def get_rightchild(self,i):
        return 2*i+2
    def has_parent(self,i):
        return self.get_parent(i) >= 0
    def has_leftchild(self,i):
        return self.get_leftchild(i) < len(self.heap)
    def has_rightchild(self,i):
        return self.get_rightchild(i) < len(self.heap)
    def swap(self,i,j):
        self.heap[i],self.heap[j] = self.heap[j],self.heap[i]
    def insert_key(self,key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) - 1)
    def heapify_up(self,i):
        size = len(self.heap)
        while(self.has_parent(i) and self.heap[i] > self.heap[self.get_parent(i)]):
            self.swap(i,self.get_parent(i))
            i = self.get_parent(i)

    def print_heap(self):
        print(self.heap)

    def delete_root(self):
        if len(self.heap) == 0:
            return -1
        last_index = len(self.heap) - 1
        self.swap(0,last_index)
        root = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_down(self, i):
        while(self.has_leftchild(i)):
            max_child = self.get_maxchild(i)
            if max_child == -1:
                break
            if (self.heap[i] < self.heap[max_child]):
                self.swap(i,max_child)
                i = max_child
            else:
                break

    def get_maxchild(self,i):
        if(self.has_leftchild(i)):
            left_c = self.get_leftchild(i)
            if(self.has_rightchild(i)):
                right_c = self.get_rightchild(i)
                if(self.heap[left_c] > self.heap[right_c]):
                    return left_c
                else:
                    return right_c
        else:
            return
max_heap = MaxHeap()
array = [45,99,63,27,29,57,42,35,12,24]

for i in array:
    max_heap.insert_key(i)

print("initial heap")
max_heap.print_heap()

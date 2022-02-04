from collections import defaultdict
from goody import type_as_str

# Iterators are covered in Week #4
# Implement all methods but iterators after Week #3

class Bag:
    def __init__(self, iterable = []):
        self.bag_dict = defaultdict(int)
        for item in iterable:
            self.bag_dict[item] += 1

    
    def __repr__(self):
        new_list = []
        if self.bag_dict == None:
            return 'Bag()'
        else:
            for key in self.bag_dict.keys():
                for _ in range(self.bag_dict[key]):
                    new_list.append(key)
        return 'Bag(' + str(new_list) + ')'
    
    def __str__(self):
        list_values = []
        new_str = ''
        if self.bag_dict == None:
            return 'Bag()'
        else:
            for key in self.bag_dict.keys():
                for _ in range(self.bag_dict[key]):
                    list_values.append(key)
        d = {x:list_values.count(x) for x in list_values}        
        for key in d.keys():
            new_str = new_str + str(key) + '[' + str(d[key]) + '],'
        return 'Bag(' + new_str[:-1] + ')'
        
    
    def __len__(self):
        return sum(self.bag_dict.values())
    
    def unique(self):
        return len(self.bag_dict)

    
    def add(self, new_item):
        self.bag_dict[new_item] +=1
        return None
    
    def __contains__(self, cont):
        return cont in self.bag_dict
            
    def count(self, value): 
        return self.bag_dict[value] if value in self else 0
    
    def __add__(self, right):
        if type(right) != type(self):
            raise TypeError
        new_bag = Bag(self)
        for item in right:
            new_bag.add(item)
        return new_bag
    
    def remove(self, value):
        if value not in self:
            raise ValueError(f"{value} not in Bag")
        self.bag_dict[value] -= 1
        if not self.bag_dict[value]:
            del self.bag_dict[value]
        return None
    
    def __eq__(self, right):
        return type(right) is type(self) and self.bag_dict == right.bag_dict
    
    def __iter__(self):       
        return (k for k, v in self.bag_dict.copy().items() for _ in range(v))        # return an object on which __next__ can be called
    
         
if __name__ == '__main__':
    #Put your own test code here to test Bag before doing bsc tests

    print('Start simple testing')

    import driver
    driver.default_file_name = 'bscp21F21.txt'
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
#     driver.default_show_traceback =True
    driver.driver()



if __name__ == '__main__':
    #Put your own test code here to test Bag before doing bsc tests
    b = Bag(['d','a','b','d','c','b','d'])
    repr(b)
    print(b)
    print('Start simple testing')

    import driver
    driver.default_file_name = 'bscp21F21.txt'
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
#     driver.default_show_traceback =True
    driver.driver()

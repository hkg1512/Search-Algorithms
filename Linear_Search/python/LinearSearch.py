
class LinearSearch:
    
    array = None
    findElement = None
    
    def __init__(self):
        pass
    
    def init(self, arr, findElement):
        self.array = arr
        self.findElement = findElement
        
    def Search(self, arr, findElement):
        
        self.init(arr,findElement)
        
        if self.array is None  or self.findElement is None:
            print("Unintialized array or findElement!")
        
        index = 0
        found = False
        
        for element in self.array:
            
            if element is self.findElement:
                found = True
                break
            
            index += 1
        
        if found is False:
            index = -1
                        
        return (found,index)

if __name__ == "__main__":
    arr = ['c','d','e']
    findElement = 'd'
    search = LinearSearch()
    found,index = search.Search(arr,findElement) 
    print("Found: " + str(found) + " Index: " + str(index))       
        
         
        
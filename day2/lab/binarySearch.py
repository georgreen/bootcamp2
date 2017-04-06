class BinarySearch(list):
    def __init__(self,length_list, step_list):
        '''
        input -> length_list : number of elem in list
             step_list   : difference between members of list
        creates a list with length elements
        '''
        self.extend(list(range(step_list, (length_list * step_list) + 1, step_list)))
        self.length = length_list

    def search(self, needle):
        '''
        input  -> needle
        output -> hay[index] = needle : index
               -> count = number of iterations
               -> return  {"count" : count, "index" : index}
        '''
        results = {"count" : 0, "index" : -1}
        low_index = 0
        high_index = self.length - 1
        
        #optimazation code(if needle is at begging or end of list) -> solves: test 112
        if self[high_index] == needle or self[low_index] == needle:
            results["index"] = self.index(needle)
            return results
        
        while(True):
            #optimaztion code(if the needle is not in range exit) -> solves : test 
            if self[low_index] > needle or self[high_index] < needle:
                results["count"] -= 1 #reduces iteration by one this didn't complete
                break
                
            midpoint = (high_index + low_index) // 2
            
            if self[midpoint] == needle:
                results["index"] = self.index(needle)
                break
            if self[midpoint] > needle:
                high_index = midpoint - 1
            if self[midpoint] < needle:
                low_index = midpoint + 1
            if high_index < low_index:
                break
            results["count"] += 1
            
        
        return results
    

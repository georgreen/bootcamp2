class BinarySearch(list):
    '''
    input -> length_list : number f elem in list
             step_list   : difference between members of list
    creates a list with length elements
    '''
    def __init__(self,length_list, step_list):
        self.extend(list(range(step_list, (length_list * step_list) + 1, step_list)))
        self.length = length_list

    def search(self, needle):
        '''
        input -> needle
        output ->hay[index] = needle : index
               -> count = number of iterations
               -> return  {"count" : count, "index" : index}
        '''
        results = {"count" : 0, "index" : -1}
        low_index = 0
        high_index = self.length - 1

        #optimazation code(if needle is at begging or end of list)
        if self[high_index] == needle or self[low_index] == needle:
            results["index"] = high_index
            return results

        while(True):
            #optimaztion code(if the needle is not in range exit)
            if self[low_index] > needle:
                results["count"] -= 1 #reduces iteration by one this didn't complete
                break
            elif self[high_index] < needle:
                results["count"] -= 1#reduce count too
                break

            #condition for halting
            if high_index >= low_index:
                mid_index = (high_index + low_index)  // 2

                #binary search logic
                if self[mid_index] == needle:
                    results["index"] = mid_index
                    results["count"] += 1 #add this cyle it breaks here
                    break
                elif needle < self[mid_index]:
                    high_index = mid_index - 1
                elif needle > self[mid_index]:
                    low_index = mid_index + 1
                #count irerations
                results["count"] =  results["count"] + 1
            else:
                break
        return results
    

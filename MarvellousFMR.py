

def filterX(Task , Elements):
    result = list ()
    
    
    for no in Elements:
        Ret = Task (no)
        
        if (Ret == True):
            result.append(no)
            
    return result

def mapx(Task ,Element):
    result = list()
      
      
    for no in Element:
        Ret = Task (no)
        result.append(Ret)
        
    return result



def reduceX(Task, Element ):
    sum = 0 
    
    #[11,21,23,31]
    for no in Element:
        Sum = Task(sum,no)
    return Sum 
        
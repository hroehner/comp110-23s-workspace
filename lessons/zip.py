"""Dictionary Practice Writing."""

__author__: "730472095"

def zip(x:list[str], y:list[int]) -> dict[str,int]: 
    """Producing a dictionary where the x list are keys, and the y list are values!"""
    end_dict: dict[int,str] = {}
    idx: int = 0
    if len(x) != len(y): 
        return {}
    if len(x) == 0 or len(y) == 0:
        return {} 
    while idx < len(x): 
        end_dict[x[idx]] = y[idx]
        idx += 1
    return end_dict 

    
    
    


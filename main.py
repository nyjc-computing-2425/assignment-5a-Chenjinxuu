def to_hms(seconds: int): #-> list:
    """
    Converts seconds to hours, minutes, and seconds, and returns it as a list.

    Parameters
    ---------
    seconds: int
        the seconds to be calculated
        
    Returns
    ---------
    list
        a list of integers representing hours, minutes, seconds

    Example:
    >>> to_hms(10)
    [0, 0, 10]
    >>> to_hms(61)
    [0, 1, 1]
    >>> to_hms(7199)
    [1, 59, 59]
    >>> to_hms(99.99)
    Unsupported input type.
    """
    # Type your code below 
   
    
    minutes = 0 
    hours = 0
  
    if "." not in str(seconds) and int(seconds) > 0 and not type(seconds)==str:
        minutes , seconds = divmod(seconds, 60)
        hours , minutes = divmod(minutes, 60)
        return [hours, minutes, seconds]
        
    else:
        return print("Unsupported input type.")

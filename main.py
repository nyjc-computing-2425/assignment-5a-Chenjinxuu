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
  
    if "." not in str(seconds) and str(seconds).isdigit() and int(seconds) > 0 and not type(seconds) == str:
        minutes , seconds = divmod(int(seconds), 60)
        hours , minutes = divmod(int(minutes), 60)
        hours = int(hours)
        result = [int(hours), int(minutes), int(seconds)]
        return print(result)
        
    else:
        return print("Unsupported input type.")

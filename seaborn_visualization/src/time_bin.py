def time_bin(x):
    '''
    Creating bins for time period
        Input: Time (hour)
        Output: Bin for time period
    '''
    if (x >= 4 and x < 10):
        return "4:00 to 10:00"
    elif (x >= 10 and x < 16):
        return "10:00 to 16:00"
    else:
        return "22:00 to 4:00"
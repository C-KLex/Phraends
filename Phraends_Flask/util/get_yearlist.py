import datetime

def get_yearlist():
    """
    Summary:
        API for frontend to get a year list for user to pick, the range will be 10 years from latest annual report
    
    Args:
        
    Returns:
        years: A list of integer that length will be 10
    """
    
    today = datetime.datetime.today()
    if today.month >= 11 :
        years = [number for number in range(today.year, today.year-10, -1)]
    else:
        years = [number for number in range(today.year-1, today.year-11, -1)]
    return years

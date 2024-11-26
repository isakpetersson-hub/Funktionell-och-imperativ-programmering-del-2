# Write your code for lab 8C (remove) here.
from cal_ui import *

def remove(calendar_name: str,day:int,month:str,start:str)->None:
    day = new_day(day)
    month = new_month(month)
    start_time = new_time_from_string(start)

    new_date(day,month)

    cal_year = get_calendar(calendar_name)
    cal_month = cy_get_month(month,cal_year)
    cal_day = cm_get_day(cal_month,day)

    if cd_is_empty(cal_day):
        return None
    
    
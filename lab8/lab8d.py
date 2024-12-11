# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT
from cal_ui import *


if CHECK_AGAINST_FACIT:
    try:
        from facit_la8_uppg import TimeSpanSeq
    except:
        print("*" * 100)
        print("*" * 100)
        print("Kan inte hitta facit; ändra CHECK_AGAINST_FACIT i test_driver.py till False")
        print("*" * 100)
        print("*" * 100)
        raise
else:
    from lab8b import *


def free_spans(cal_day: CalendarDay, start: Time, end: Time) -> TimeSpanSeq:
    free_time=[]
    # cal_day.sort()
    iter_start=start
    if cd_is_empty(cal_day):
        free_time.append((start,end))
    else:
        for appointment in cd_iter_appointments(cal_day):
            time_span = appointment.span
            appointment_start = ts_start(time_span)
            appointment_end = ts_end(time_span)

            if iter_start<appointment_start<end:
                free_time.append((iter_start,appointment_start))
                iter_start=appointment_end
            elif iter_start<appointment_end:
                iter_start=appointment_end
        if appointment_end<end:
            free_time.append((appointment_end,end))  
    return free_time

def show_free(calendar_name: str,day:int,month:str,start:str, end: str):

    day = new_day(day)
    month = new_month(month)
    start_time = new_time_from_string(start)
    end_time = new_time_from_string(end)
    new_date(day,month)

    cal_year = get_calendar(calendar_name)
    cal_month = cy_get_month(month,cal_year)
    cal_day = cm_get_day(cal_month,day)

    list = free_spans(cal_day, start_time, end_time)
    for (itr_start_time,itr_end_time) in list:
        # start_hour,start_minute=start_time
        # end_hour,end_minute=end_time
        show_ts(new_time_span(itr_start_time,itr_end_time))
        print("")

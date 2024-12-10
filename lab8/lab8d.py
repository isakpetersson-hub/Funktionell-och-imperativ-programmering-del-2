# Write your code for lab 8d here.
from cal_abstraction import CalendarDay, Time
from settings import CHECK_AGAINST_FACIT

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
    cal_day.sort()
    iter_start=start
    for appointment in cd_iter_appointments(cal_day):
        time_span = appointment.span
        appointment_start = ts_start(time_span)
        appointment_end = ts_end(time_span)
        if iter_start<appointment_start<end:
            free_time.append((start,appointment_start))
        if appointment_end>iter_start:
            iter_start=appointment_end
    
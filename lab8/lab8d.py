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
      
    print(free_time)
    return free_time

day = new_day(20)

Appointment2 = new_appointment(new_time_span(new_time(new_hour(13),new_minute(00)),new_time(new_hour(15),new_minute(00))),new_subject("test"))
Appointment = new_appointment(new_time_span(new_time(new_hour(10),new_minute(00)),new_time(new_hour(11),new_minute(00))),new_subject("test"))

calendarday=new_calendar_day(day,[Appointment])

# create("test")
# book("test",20,"jan","12:00","14:00","klyva atomer")
# book("test",20,"jan","15:00","17:00","uppfinna atombomben")

print(free_spans(calendarday,new_time_from_string("08:00"),new_time_from_string("21:00")))

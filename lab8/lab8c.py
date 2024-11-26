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
        print("No appointments during this day")
        return None
    
    for appointment in cd_iter_appointments(cal_day):
        time_span = appointment.span
        if time_equals(ts_start(time_span),start_time):
            cal_day.appointments.remove(appointment)
            new_year=plus_appointment(cal_year,cal_day,cal_month,start_time,None,None)
            insert_calendar(calendar_name,new_year)
            print("Appointment has been removed")
            break
        else:
            print("No appointment found at the specified time")

create("test")
book("test",20,"jan","12:00","14:00","klyva atomer")
book("test",20,"jan","13:00","14:00","nu bliddere fel")
book("test",20,"jan","15:00","17:00","uppfinna atombomben")
show("test",20,"jan")
remove("test",20,"jan","15:00")


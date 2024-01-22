from datetime import datetime
from icalendar import Calendar, Event

#you will have to scrape the json file and convert it to a list of dictionaries

all_calendars = []
cal = Calendar()

for item in all_calendars:
    event = Event()
    event.add('uid', item['id'])
    event.add('summary', item['title'])

    # Parse the start and end date-time and format it properly for iCalendar
    start_datetime = datetime.strptime(item['start'], '%Y-%m-%d %H:%M')
    end_datetime = datetime.strptime(item['end'], '%Y-%m-%d %H:%M')

    event.add('dtstart', start_datetime)
    event.add('dtend', end_datetime)

    cal.add_component(event)

# Write to file
file_path = 'my_calendar.ics'
with open(file_path, 'wb') as f:
    f.write(cal.to_ical())

print(f"iCalendar file created at: {file_path}")

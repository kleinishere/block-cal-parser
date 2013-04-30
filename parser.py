from icalendar import Calendar

def process_file(file):
    "Processes the iCal file looking for lecture names."

    calendar = Calendar.from_ical(open(file, 'rb').read())

    lecture_names = []
    
    for component in calendar.walk():
        if component.name == "VEVENT" and \
        component.get('LOCATION') == 'CHS 73-105':
            lecture_name = str(component.get('summary'))
            lecturer_placeholder = lecture_name.find(' (')
            lecture_names.append(lecture_name[0:lecturer_placeholder])

    return lecture_names

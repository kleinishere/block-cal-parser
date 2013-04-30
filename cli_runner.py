from sys import argv, exit
from time import sleep

from parser import process_file

script_version = 0.1

# Formatting
prompt = '> '
line_break = '-=-' * 20

# Script arguments
script, calendar_file = argv

print line_break
print "Welcome to %s v%s" % (script, str(script_version))
print line_break, "\n"

sleep(1)

print 'Processing "%s"...\n' % (calendar_file)

list = process_file(calendar_file)

if list:
    print "Success!\n"
    sleep(1)
else:
    print "File unable to be read."
    exit(1)

print 'What output would you like?\n'
print '1 for onscreen. 2 for output.txt\n'

output_choice = raw_input(prompt)

if output_choice not in ['1', '2']:
    print 'Wrong answer choice. Please try script again.'
    exit(0)

elif output_choice == '1':
    print 'Good choice.'

    i = 1

    for lecture_name in list:

        print i, ')', lecture_name
        i += 1

elif output_choice == '2':
    target = open('output.txt', 'w')
    target.truncate()

    i = 1

    for lecture_name in list:
        lecture_name_formatted = str(i) + ') ' + lecture_name + "\n"
        target.write(lecture_name_formatted)

        i += 1

    target.close()

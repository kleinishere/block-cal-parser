from sys import argv

script_version = 0.1

# Formatting
prompt = '> '
line_break = '-=-' * 4

# Script arguments
script, calendar_file = argv

print line_break
print "Welcome to %s v%s" % (script, str(script_version))
print line_break
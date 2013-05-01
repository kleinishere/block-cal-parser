# Block Calendar Parser

![Imgur](http://i.imgur.com/ZyC5BUI.png "Block 5")

Given the block ICS file (acquired from ANGEL), this script generates a text list of lecture names comprising the block at UCLA DGSOM.

## Assumptions

Only includes calendar events with location of 'CHS 73-105'.

## Instructions

Run with:

> python cli_runner.py name_of_calendar.ics

## ToDos

* Only extract events finishing before 1:01PM to avoid afternoon sessions.
* Add week counting, followed by lecture number counting. "L1-First Lecture Name"
* Add lecture name grabbing and option to include lecturer name in output.
* Refine module structure to be more direct in its use and returns.
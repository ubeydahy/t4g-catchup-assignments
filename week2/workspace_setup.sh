#!/bin/bash

#greeting
name="Ubeydah"
greeting="Hello there"
echo "$greeting, my name is $name"

#Showing current date and time
echo "Current date and time:" $(date)

#Creating session log folder
mkdir -p session_logs

#Creating a log file inside session_logs/ named with today's date(Using command substition with date)
log_file="session_logs/$(date +%Y-%m-%d).log"

#Writing my name and a brief note into the log file
echo "$name" > $log_file
echo "This is my workspace setup log." >> $log_file

#Setup Complete
echo "Setup complete!"




#!/usr/bin/env ruby
#  Regular expression to parse log file
#  The script should outputs: [SENDER],[RECEIVER],[FLAGS]
#  The sender phone number or name (including country code if present)
#  The receiver phone number or name (including country code if present)
#  The flags that were used
print ARGV[0].scan(/\bfrom:(\S*)\b/).join + ","
print ARGV[0].scan(/\bto:(\S*)\b/).join + ","
print ARGV[0].scan(/\bflags:(\S*)\b/).join + "\n"

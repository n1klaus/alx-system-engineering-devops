#!/usr/bin/env ruby
#  Regular expression to match string that starts with h ends with n
#+ and can have any single character in between
puts ARGV[0].scan(/^h[\d\w]{1}n$/).join

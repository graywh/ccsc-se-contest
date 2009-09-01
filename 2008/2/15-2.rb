#!/usr/bin/env ruby

STDIN.readline
STDIN.readlines.each do |line|
  sum = 0
  line.strip!
  while line.length > 0
    case line
    when /IV/
      line.sub!(/IV/, '')
      sum += 4
    when /IX/
      line.sub!(/IX/, '')
      sum += 9
    when /XL/
      line.sub!(/XL/, '')
      sum += 40
    when /XC/
      line.sub!(/XC/, '')
      sum += 90
    when /CD/
      line.sub!(/CD/, '')
      sum += 400
    when /CM/
      line.sub!(/CM/, '')
      sum += 900
    when /I/
      line.sub!(/I/, '')
      sum += 1
    when /V/
      line.sub!(/V/, '')
      sum += 5
    when /X/
      line.sub!(/X/, '')
      sum += 10
    when /L/
      line.sub!(/L/, '')
      sum += 50
    when /C/
      line.sub!(/C/, '')
      sum += 100
    when /D/
      line.sub!(/D/, '')
      sum += 500
    when /M/
      line.sub!(/M/, '')
      sum += 1000
    end
  end
  puts sum
end

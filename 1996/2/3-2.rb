#!/usr/bin/env ruby

DAYSINMONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS = %w( Sunday Monday Tuesday Wednesday Thursday Friday Saturday )

def jan1(m, d, y)
  ((36 + (y - 1) + ((y - 1) / 4) - ((y - 1) / 100) + ((y - 1) / 400)) % 7)
end

def leap(y)
  ((((y % 4) == 0) and ((y % 100) != 0)) or ((y % 400) == 0))
end

def validDay(m, d, y)
  (DAYSINMONTH[m - 1] + ((leap(y) and m == 2) ? 1 : 0))
end

def valid(m, d, y)
  ((m > 0) and (m <= 12) and (d > 0) and (d <= validDay(m, d, y)) and (y > 0))
end

STDIN.readlines.each do |line|
  m, d, y = line.strip.split('/').collect { |x| x.to_i }
  if not valid(m, d, y)
    puts "Invalid date in the input."
  else
    dp = DAYSINMONTH[0,m-1].inject(:+) + d + jan1(m, d, y) - 1
    puts "#{m}/#{d}/#{y} falls on a #{DAYS[dp % 7]}"
  end
end

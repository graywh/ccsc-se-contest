#!/usr/bin/env ruby

file = File.open('buffy.dat')
msg = 1
while true
  begin
    line = file.readline
  rescue EOFError
    break
  end
  rows, cols = line.split.collect { |x| x.to_i }
  ary = []
  rows.times { ary << file.readline.split }
  print "Message #{msg} => "
  j = cols
  0...rows.each do |i|
    print ary[i][j-1]
    print ' '
    j -= 1
    j = cols if j == 0
  end
  puts
  msg += 1
end

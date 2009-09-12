#!/usr/bin/env ruby

puts "Z  I  M  L  Length"
puts "------------------"

STDIN.each do |line|
  line = line.split
  z, i, m, l = line.collect { |i| i.to_i }
  count = 0
  print "%s %s %s %s" % line.collect { |p| p.ljust(2) }
  start =  ((z * l + i) % m)
  l = ((z * l + i) % m)
  if m == 1
    puts "ERROR"
  else
    while true do
      l = ((z * l + i) % m)
      count += 1
      break if start == l
    end
    puts count.to_s.rjust(3)
  end
end

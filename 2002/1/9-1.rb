#!/usr/bin/env ruby

STDIN.readlines.each do |line|
  a,b,c,n = line.split(',').collect { |i| i.to_i }
  total = a + b + c
  (n-3).times do
    d = a + b + c
    total += d
    a,b,c = b,c,d
  end
  puts "The answer is: #{total}"
end

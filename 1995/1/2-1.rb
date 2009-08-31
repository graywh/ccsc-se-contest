#!/usr/bin/env ruby

File.readlines('prob1.in').each do |line|
  a,b = line.split().collect { |n| n.to_i }
  print "#{a} * #{b} = "
  sum = 0
  while a > 0
    if a % 2 > 0
      print b
      sum += b
      print " + " if a > 1
    end
    a /= 2
    b *= 2
  end
  print " = #{sum}"
  puts
end

#!/usr/bin/env ruby

ORDER = {
  4 => 0,
  8 => 1,
  3 => 2,
  7 => 3,
  2 => 4,
  6 => 5,
  1 => 6,
  5 => 7
}

STEPS = %w( up down )

STDIN.readline.to_i.times do |i|
  line = STDIN.readline
  print "Case #{i+1}: "
  f, t = line.split.collect { |i| ORDER[i.to_i] }
  if f < t
    (f...t).each { |j| print STEPS[j%2] + ' ' }
    puts
  else
    puts "Take the stairs!"
  end
end

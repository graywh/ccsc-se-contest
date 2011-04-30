#!/usr/bin/env ruby

STDIN.each do |line|
  x = line.to_i
  y = x / 60
  z = x % 60
  total = y / 2 * 300
  if y % 2 == 0
    total += z * 15
  else
    total += 900
    total -= z * 10
  end
  puts total if x <= 720 and x >= 0
end

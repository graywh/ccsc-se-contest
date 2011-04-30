#!/usr/bin/env ruby

def count(n, m, so_far=[])
  l = so_far.length
  if l == n
    c = 1
  else
    if l == 0
      a = 1
    else
      a = so_far[-1] * 2
    end
    b = (m / 2**(n-l-1)).to_i
    if b < a
      c = 0
    else
      c = (a..b).collect do |x|
        count(n, m, so_far + [x])
      end.inject(&:+)
    end
  end
  return c
end

STDIN.readline.to_i.times do |i|
  lines = STDIN.readline
  n, m = line.split.collect(&:to_i)
  number = count(n, m)
  puts "Data set #{i+1}: #{n} #{m} #{number}"
end

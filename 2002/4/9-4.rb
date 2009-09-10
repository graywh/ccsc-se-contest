#!/usr/bin/env ruby

STDIN.readlines.each do |line|
  count = 0
  x = 1
  line.chars do |c|
    if x >= 0
      count += 1
      if c == 'e'
        x += 1
      else
        x -= 1
      end
    end
  end
  puts (x >= 0 ? -1 : count)
end

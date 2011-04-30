#!/usr/bin/env ruby

STDIN.readline.to_i.times do
  line = STDIN.readline
  problem = line.split.collect { |n| n.to_i }
  puts 1 - problem[0] + problem[1..-1].inject(:+)
end

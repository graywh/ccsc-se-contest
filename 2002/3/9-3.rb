#!/usr/bin/env ruby

STDIN.each do |line|
  groups = []
  count = 0
  line.chars do |c|
    if c == 'A'
      count += 1
    else
      groups << count if count > 0
      count = 0
    end
  end
  groups << count if count > 0
  puts groups.uniq.length
end

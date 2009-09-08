#!/usr/bin/env ruby

def needed(x, p)
  s = x.inject(:+)
  mn, md, mx = x.sort
  if s - mx > p
    nil
  elsif mx + mn > p
    2 * (mx + mn)
  elsif 2 * (mx + mn) > p
    2 * (md + mn)
  else
    mn + md
  end
end

paper = STDIN.readline.split[2].to_i
STDIN.readline

count = 1
STDIN.readlines.each do |line|
  print "Gift #{count} "
  d = line.split('x').collect { |a| a.to_i }
  n = needed(d, paper)
  if n
    puts "needs #{n} inches."
  else
    puts "cannot be wrapped."
  end
  count += 1
end

#!/usr/bin/env ruby

def f(friends, m, list)
  if m == 0
    puts list.join(' ')
  elsif friends.length > 0
    f(friends[1..-1], m - 1, list + friends[0..0])
    f(friends[1..-1], m, list)
  end
end

STDIN.readline.to_i.times do |n|
  puts "Text case #{n+1}:"
  n, m = STDIN.readline.split.map(&:to_i)
  friends = []
  n.times { friends << STDIN.readline.strip }
  friends.sort!
  f(friends, m, [])
  puts ""
end

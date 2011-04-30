#!/usr/bin/env ruby

count = Hash.new(0)
STDIN.each do |line|
  state, votes, name = line.split
  count[name] += votes.to_i
end
winner = count.sort_by { |k,v| -v } [0]
puts "#{winner[0]} wins with #{winner[1]} votes"

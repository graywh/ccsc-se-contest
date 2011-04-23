#!/usr/bin/env ruby

data = {}

def rating(win,loss,sum)
  (sum + 400.0 * (win - loss)) / (win + loss)
end

STDIN.readline
STDIN.readlines.each do |line|
  team, record, scores = line.split(' ', 3)
  wins, loss = record.split('-').map(&:to_i)
  sum = scores.split.map(&:to_i).inject(&:+)
  data[team] = rating(wins,loss,sum)
end

data.sort { |a,b| b[1] <=> a[1] }.each_with_index do |(team, score), i|
  puts "#{i+1})#{team} #{"%.2f" % score}"
end

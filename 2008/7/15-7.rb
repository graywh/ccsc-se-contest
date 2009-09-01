#!/usr/bin/env ruby

while true
  x = STDIN.readline.to_i
  break if x == -1
  clas = {}
  x.times do
    name, a, b, c = STDIN.readline.split
    clas[name] = a.to_i * 5 + b.to_i * 10 + c.to_i * 20
  end
  clas = clas.sort_by { |k,v| v }
  if clas[0][1] == clas[-1][1]
    puts "All have the same amount"
  else
    puts "#{clas[-1][0]} has most, #{clas[0][0]} has least money."
  end
end

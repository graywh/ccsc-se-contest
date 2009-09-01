#!/usr/bin/env ruby

File.readlines('mono.in').each do |line|
  mono = true
  up = line[0,1] < line[1,1]
  (2..(line.length-2)).each do |i|
    if (up and line[i,1] >= line[i+1,1]) or (!up and line[i,1] <= line[i+1,1])
      mono = false
      break
    end
  end
  puts line if mono
end

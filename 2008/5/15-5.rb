#!/usr/bin/env ruby

BLOC = /\(([RD]{3})\)/

STDIN.readline.to_i.times do |i|
  line = STDIN.readline
  while line =~ BLOC
    line.sub!(BLOC) { |s| $1.chars.sort[1] }
  end
  puts "Case #{i+1}: #{line}"
end

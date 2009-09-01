#!/usr/bin/env ruby

BLOC = /\(([RD]{3})\)/

count = 1
STDIN.readline
STDIN.readlines.each do |line|
  while line =~ BLOC
    line.sub!(BLOC) { |s| $1.chars.sort[1] }
  end
  puts "Case #{count}: #{line}"
  count += 1
end

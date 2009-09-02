#!/usr/bin/env ruby

BLOC = /\(([RD]{3})\)/

STDIN.readline
STDIN.readlines.each_with_index do |line, i|
  while line =~ BLOC
    line.sub!(BLOC) { |s| $1.chars.sort[1] }
  end
  puts "Case #{i+1}: #{line}"
end

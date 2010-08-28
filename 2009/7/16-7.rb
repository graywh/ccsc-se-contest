#!/usr/bin/env ruby

STDIN.readlines.each do |line|
  line =~ /R([0-9]*)C([0-9]*)/
  row = $1.to_i
  column = $2.to_i
  break if row == 0 && column == 0
  column -= 1
  col = (65 + column % 26).chr
  column = column / 26 - 1
  while column >= 0
    col += (65 + column % 26).chr
    column = column / 26 - 1
  end
  puts "#{col.reverse}#{row}"
end

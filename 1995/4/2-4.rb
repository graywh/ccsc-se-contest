#!/usr/bin/env ruby

chk = [1,0,0,0,0,0,1]
File.readlines('prob4.in').each do |line|
  line = line.strip.chars.collect { |c| c.to_i }
  recording = false
  line.each_slice(7) do |slice|
    if slice == chk
      recording = !recording
    elsif recording
      sum = 0
      slice.each_with_index { |a,j| sum += a * (2 ** (6 - j)) }
      print sum.chr
    end
  end
  puts
end

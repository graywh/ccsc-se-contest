#!/usr/bin/env ruby

require 'date'

STDIN.readlines.each do |line|
  puts (Date.new(1900 + line[0...2].to_i, 1, 1) + line[2..-1].to_i - 1).strftime("%m/%d/%Y")
end

#!/usr/bin/env ruby

SYMBOLS = /[&.:;?!-()]/

count = STDIN.readlines.collect { |line| line.strip.gsub(SYMBOLS, '').split.length } .inject(:+)
puts "This file contains #{count} words."

#!/usr/bin/env ruby

SYMBOLS = /[&.:;?!-()]/

count = File.readlines('words.txt').collect { |line| line.strip.gsub(SYMBOLS, '').split.length } .inject(:+)
puts "This file contains #{count} words."

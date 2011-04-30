#!/usr/bin/env ruby

DAT = %w( monkey rooster dog pig rat ox tiger rabbit dragon snake horse sheep ).freeze

def get_animal(year)
  DAT[year % 12]
end

STDIN.readline.to_i.times do |year|
  puts "#{year.strip} is the year of the #{get_animal(year.to_i)}"
end

#!/usr/bin/env ruby

require 'date'

STDIN.readlines.each do |line|
  begin
    puts "#{line.strip} falls on a #{Date::DAYNAMES[Date.parse(line).wday]}"
  rescue
    puts "Invalid date in the input."
  end
end

#!/usr/bin/env ruby

require 'date'

STDIN.readline.to_i.times do
  line = STDIN.readline
  locale, time = line.split('=')
  case locale
  when 'Paris'
    time = DateTime.parse(time) - Rational(1,4)
    locale = 'Roanoke'
  when 'Roanoke'
    time = DateTime.parse(time) + Rational(1,4)
    locale = 'Paris'
  end
  puts "The time in #{locale} is now #{time.strftime('%l:%M %p').lstrip}"
end

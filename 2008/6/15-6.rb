#!/usr/bin/env ruby

STDIN.readlines[0...-1].each_slice(2) do |code,line|
  shift, opp = code.split
  case opp
  when 'D'
    e = 'z'[0] - shift.to_i
    s = e + 1
  when 'E'
    s = 'a'[0] + shift.to_i
    e = s - 1
  end
  tr = "#{s.chr}-za-#{e.chr}"
  line.tr!('a-z', tr)
  line.tr!('A-Z', tr.upcase)
  puts line
end

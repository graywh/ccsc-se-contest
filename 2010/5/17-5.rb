#!/usr/bin/env ruby

STDIN.readlines.each do |line|
  break if line.strip == "#"

  tokens = line.split
  op = tokens[-2]
  text = tokens[-1]
  key = tokens[0...-2].map(&:to_i)
  res = ''
  (0...(key.length)).each do |i|
    case op
    when 'E'
      s = 'a'[0] + key[i]
      e = s - 1
    when 'D'
      e = 'z'[0] - key[i]
      s = e + 1
    end
    tr = "#{s.chr}-za-#{e.chr}"
    res << text[i..i].tr('a-z', tr).tr('A-Z', tr.upcase)
  end
  puts res
end

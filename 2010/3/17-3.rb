#!/usr/bin/env ruby

TAU = Math::PI * 2

STDIN.readline.to_i.times do
  p = [0,1]
  r = Math.sqrt(1)
  th = 0
  (STDIN.readline.to_i - 1).times do |n|
    th += Math.atan(1 / r)
    r = Math.sqrt(n + 2)
    p[0] = r * Math.cos(th)
    p[1] = r * Math.sin(th)
  end
  puts "%.4f %.4f" % p
end

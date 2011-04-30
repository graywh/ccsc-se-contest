#!/usr/bin/env ruby

def x(p)
  p[0]
end

def y(p)
  p[1]
end

def area(p1, p2, p3)
  0.5 * ( (x(p1) * y(p2)) + (x(p2) * y(p3)) + (x(p3) * y(p1)) - (x(p1) * y(p3)) - (x(p2) * y(p1)) - (x(p3) * y(p2)))
end

STDIN.readline
points = STDIN.collect do |line|
  line.split(',').collect do |i|
    i.to_i
  end
end

hull = []
p0 = points[0]
points.each do |p|
  p0 = p if y(p) < y(p0)
end
start = p0
hull << p0

pn = nil
while true
  points.each do |p1|
    next if p1 == p0
    x = points.collect do |p2|
      #puts "(%s,%s) (%s,%s) (%s,%s)" % [p0,p1,p2].flatten
      area(p0, p1, p2) >= 0
    end.all?
    if x
      pn = p1
    end
  end
  break if pn == start or pn.nil?
  hull << pn
  p0 = pn
end

hull.each { |p| puts "(%s,%s)" % p }

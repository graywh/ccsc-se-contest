#!/usr/bin/env ruby

class Node
  attr_reader :value

  def initialize(v = " ")
    @value = v
    @child = []
  end

  def empty?
    @child.empty?
  end

  def <<(x)
    @child << x
  end

  def length
    @child.length
  end

  def [](i)
    @child[i]
  end
end

def match(name = "", n = 1, names = [], bill = [])
  name = name + bill[n-1].value
  if bill[n-1].empty?
    names << name
  else
    bill[n-1].length.times do |i|
      match(name, bill[n-1][i], names, bill)
    end
  end
end

count = 1
until STDIN.eof do
  line = STDIN.readline
  break if line.empty?
  names = []
  num, m, v = line.split
  num = num.to_i
  m = m.to_i
  bill = [nil] * num
  bill[0] = Node.new(v)
  m.times do |i|
    p, num, s, v = STDIN.readline.split
    p = p.to_i
    num = num.to_i
    bill[num - 1] = Node.new(v)
    bill[p - 1] << num
  end
  match("", 1, names, bill)
  full = 1
  part = 0
  names.each do |name|
    full = 0 if name != names[0]
    part = 1 if names.count(name) > 1
  end
  print "Sample #{count}: "
  if full == 1
    puts "Exact match - summon the grand jury."
  elsif part == 1
    puts "Partial match - close, but no cigar."
  else
    puts "No match - sorry, Ken."
  end
  count += 1
end

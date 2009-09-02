#!/usr/bin/env ruby

class WoodChuck
  attr_accessor :tooth, :name

  def initialize(name, tooth)
    @name = name
    @tooth = tooth.to_i
  end

  def <=>(wc)
    @tooth <=> wc.tooth
  end
end

list = []
STDIN.readlines.each do |line|
  n,t = line.split()
  list << WoodChuck.new(n, t)
end
list.sort.each do |wc|
  puts "#{wc.name} the woodchuck can chuck #{wc.tooth * 5} kilograms of wood."
end

#!/usr/bin/env ruby

def clear(grid, dim, x, y)
  grid[x][y] = 0
  (-1..1).each do |i|
    (-1..1).each do |j|
      clear(grid, dim, x+i, y+j) if dim.include?(x+i) and dim.include?(y+j) and grid[x+i][y+j] != 0
    end
  end
end

file = File.new('prob2_in.txt')
targets = 0
dim = 0...file.readline.to_i
grid = file.readlines.collect do |line|
  line.chars.collect { |c| c.to_i }
end
dim.each do |i|
  dim.each do |j|
    if grid[i][j] != 0
      targets += 1
      clear(grid, dim, i, j)
    end
  end
end
puts "There are #{targets} targets in the current image."

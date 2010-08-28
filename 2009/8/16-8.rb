#!/usr/bin/env ruby

n = STDIN.readline.to_i
x = STDIN.readline.split.collect(&:to_f)
y = STDIN.readline.split.collect(&:to_f)
sum_x = x.inject(:+)
mean_x = sum_x / n
sum_y = y.inject(:+)
mean_y = sum_y / n
std_x = 0
std_y = 0
sum_pairs = 0
(0...n).each do |i|
  std_x += (x[i] - mean_x) ** 2
  std_y += (y[i] - mean_y) ** 2
  sum_pairs += x[i] * y[i]
end
std_x = (std_x / (n - 1)) ** 0.5
std_y = (std_y / (n - 1)) ** 0.5
corr = (sum_pairs - n * mean_x * mean_y) / ((n - 1) * std_x * std_y)
puts "The correlation between your X and Y variables is #{(100*corr).round / 100.0}."

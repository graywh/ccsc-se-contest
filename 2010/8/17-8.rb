#!/usr/bin/env ruby

def clicked?(cursor, window)
  cursor[0] >= window[0] && cursor[0] <= (window[0] + window[3] - 1) &&
    cursor[1] >= window[1] && cursor[1] <= (window[1] + window[2] - 1)
end

counter = 0
while (nw = STDIN.readline.to_i) > 0
  counter += 1
  puts "Desktop #{counter}:"
  windows = []
  nw.times do
    windows << STDIN.readline.split.map(&:to_i)
  end
  windows.reverse!
  nc = STDIN.readline.to_i
  nc.times do
    background = true
    cursor = STDIN.readline.split.map(&:to_i)
    windows.each_with_index do |window, i|
      if clicked?(cursor, window)
        puts "Window #{nw - i}"
        background = false
        break
      end
    end
    puts "background" if background
  end
end

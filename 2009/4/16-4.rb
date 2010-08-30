#!/usr/bin/env ruby

scores = []
STDIN.readline
STDIN.readlines.each do |line|
  line = line.split.reverse
  name = line.pop
  throws = line.collect(&:to_i)
  score = 0
  (0...10).each do |i|
    frame = throws.pop
    if frame == 10
      score += frame + throws[-1] + throws[-2]
    else
      frame += throws.pop
      if frame == 10
        score += frame + throws[-1]
      else
        score += frame
      end
    end
  end
  scores.push [name,score.to_s]
end

scores.sort { |a,b| a[1] <=> b[1] }.each do |name, score|
  puts "#{name.ljust(14)} #{score.rjust(3)}"
end

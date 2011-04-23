#!/usr/bin/env ruby

PTS = {
  'A' => 4,
  'B+' => 3.5,
  'B' => 3,
  'C+' => 2.5,
  'C' => 2,
  'D' => 1,
  'F' => 0
}

def grade?(grade)
  PTS.key?(grade)
end

def pass?(grade)
  !['F','U'].include?(grade)
end

STDIN.readline.to_i.times do
  name, count = STDIN.readline.split
  grade_hours = 0
  credit_hours = 0
  qual_pts = 0
  count.to_i.times do
    course, grade, hours = STDIN.readline.split
    hours = hours.to_i
    if grade?(grade)
      qual_pts += PTS[grade] * hours
      grade_hours += hours if pass?(grade)
    else
      credit_hours += hours if pass?(grade)
    end
  end
  puts "#{name} has earned #{grade_hours + credit_hours} hours with a GPA of #{"%.2f" % (qual_pts / grade_hours)}"
end

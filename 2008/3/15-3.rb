#!/usr/bin/env ruby

THEAAN = /\A(The|A|An)\s+(.*)\Z/

db = Hash.new { |hash, key| hash[key] = [] }
STDIN.readlines.each do |line|
  year, title = line.split(' ', 2)
  title = $2 + ', ' + $1 if title =~ THEAAN
  db[year] << title
end
db.sort_by { |k,v| -(k.to_i) } .each do |year,list|
  list.sort.each do |title|
    puts title
  end
end

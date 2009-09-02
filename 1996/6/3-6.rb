#!/usr/bin/env ruby

TRASH = /([,.!?:;\n])\Z/
SWAP = /\A(.*)([TtKkWwSs]h|[Tt]r|[Ff]l)\Z/

File.readlines('pig.dat').each do |line|
  line.split.each do |word|
    word = word.gsub(TRASH, '')
    ending = $1.nil? ? '' : $1
    word = word[0...-2]
    if word =~ SWAP
      word = $2 + $1
    elsif word[-1,1] == 'y'
      word = word[0...-1]
    else
      word = word[-1,1] + word[0...-1]
    end
    print word + ending + ' '
  end
  puts
end

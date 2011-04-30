#!/usr/bin/env ruby

def prefix(word)
  case word
  when /\banti(\w*)/
    ['against #{word}', $1]
  when /\bpost(\w*)/
    ['after #{word}', $1]
  when /\bpre(\w*)/
    ['before #{word}', $1]
  when /\bre(\w*)/
    ['#{word} again', $1]
  when /\bun(\w*)/
    ['not #{word}', $1]
  else
    ['#{word}', word]
  end
end

def suffix(word)
  case word
  when /(\w*)er\b/
    ['one who #{word}s', $1]
  when /(\w*)ing\b/
    ['to actively #{word}', $1]
  when /(\w*)ize\b/
    ['change into #{word}', $1]
  when /(\w*)s\b/
    ['multiple instances of #{word}', $1]
  when /(\w*)tion\b/
    ['the process of #{word}ing', $1]
  else
    ['#{word}', word]
  end
end

STDIN.readline.to_i.times do
  word = STDIN.readline
  string1, word = prefix(word)
  string2, word = suffix(word)
  word = eval('"' + string2 + '"')
  word = eval('"' + string1 + '"')
  puts word
end

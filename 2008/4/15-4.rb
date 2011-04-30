#!/usr/bin/env ruby

FROM = /\bfrom (\S*) (\S*)\b/
IN = /\bin (\S*) (\S*)\b/
INTO = /\binto (\S*) (\S*)\b/
ON = /\bon (\S*) (\S*)\b/
ONTO = /\bonto (\S*) (\S*)\b/

VOWEL = {
  'from' => 'sta',
  'in'   => 'ssa',
  'into' => 'n',
  'on'   => 'lla',
  'onto' => 'lle'
}

CONSONANT = {
  'from' => 'ista',
  'in'   => 'issa',
  'into' => 'oon',
  'on'   => 'illa',
  'onto' => 'ille'
}

def wordend(word, preposition, dup=false)
  case word
  when /\Aa|the\Z/
    word
  when /[aeiouy]\Z/
    word + (dup ? word[-1,1] : '') + VOWEL[preposition]
  else
    word + CONSONANT[preposition]
  end
end

STDIN.readline.to_i.times do
  line = STDIN.readline
  catch(:redo) do
    case line
    when FROM
      word1 = $1
      word2 = $2
      word1 = wordend(word1, 'from')
      word2 = wordend(word2, 'from')
      line.sub!(FROM, word1 + ' ' + word2)
      redo
    when IN
      word1 = $1
      word2 = $2
      word1 = wordend(word1, 'in')
      word2 = wordend(word2, 'in')
      line.sub!(IN, word1 + ' ' + word2)
      redo
    when INTO
      word1 = $1
      word2 = $2
      word1 = wordend(word1, 'into', true)
      word2 = wordend(word2, 'into', true)
      line.sub!(INTO, word1 + ' ' + word2)
      redo
    when ON
      word1 = $1
      word2 = $2
      word1 = wordend(word1, 'on')
      word2 = wordend(word2, 'on')
      line.sub!(ON, word1 + ' ' + word2)
      redo
    when ONTO
      word1 = $1
      word2 = $2
      word1 = wordend(word1, 'onto')
      word2 = wordend(word2, 'onto')
      line.sub!(ONTO, word1 + ' ' + word2)
      redo
    end
  end
  line.gsub!(/\b(a|the)\b/, '')
  line.gsub!(/ +/, ' ')
  line.gsub!(/\A +/, '')
  line.sub!(/\Z/, '.') if line =~ /[^.]\Z/
  line.capitalize!
  puts line
end

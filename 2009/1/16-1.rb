#!/usr/bin/env ruby

TO_WORD = {
  1 => 'one',
  2 => 'two',
  3 => 'three',
  4 => 'four',
  5 => 'five',
  6 => 'six',
  7 => 'seven',
  8 => 'eight',
  9 => 'nine',
  10 => 'ten',
  11 => 'eleven',
  12 => 'twelve',
  13 => 'thirteen',
  14 => 'fourteen',
  15 => 'fifteen',
  16 => 'sixteen',
  17 => 'seventeen',
  18 => 'eighteen',
  19 => 'nineteen',
  20 => 'twenty',
  30 => 'thirty',
  40 => 'forty',
  50 => 'fifty',
  60 => 'sixty',
  70 => 'seventy',
  80 => 'eighty',
  90 => 'ninety',
}

def to_words(number)
  words = []
  names = ['', 'thousand', 'million', 'billion'].reverse
  while number > 0
    three = number % 1000
    number /= 1000
    if three > 0
      words.push names.pop
      words.push to_words_3(three)
    else
      words.push ''
    end
  end
  words.reverse.join(' ').gsub(/ +/, ' ').strip
end

def to_words_3(number)
  [to_words_hundreds(number), to_words_tens(number)].join(' ')
end

def to_words_hundreds(number)
  if number > 100
    "#{to_words_ones(number/100)} hundred"
  else
    ''
  end
end

def to_words_tens(number)
  ten = number % 100
  if TO_WORD.has_key?(ten)
    TO_WORD[ten]
  else
    a = TO_WORD[(ten / 10) * 10]
    if (ten % 10) > 0
      [a, TO_WORD[ten % 10]].join('-')
    else
      a
    end
  end
end

def to_words_ones(number)
  TO_WORD[number % 10]
end

STDIN.readline
STDIN.readlines.each do |line|
  dollars, cents = line.split('.').collect(&:to_i)
  word_dollars = to_words(dollars)
  if cents > 0
    word_dollars += " and #{cents}/100"
  end
  word_dollars += ' dollar'
  if dollars > 0 && cents > 0
    word_dollars += 's'
  end
  puts word_dollars
end

ups = { '0' => '0',
        '1' => '1',
        '2' => '2',
        '3' => 'x',
        '4' => 'x',
        '5' => '5',
        '6' => '9',
        '7' => 'x',
        '8' => '8',
        '9' => '6',
      }

STDIN.readline.to_i.times do
  line = STDIN.readline
  line.strip!
  print "#{line}: "
  puts (line == line.chars.collect { |c| ups[c] } .reverse.join('') ? 'Yes' : 'No')
end

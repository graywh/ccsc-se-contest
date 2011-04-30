#!/usr/bin/env ruby

KEYS = {
  'a' => '2', 'b' => '22', 'c' => '222',
  'd' => '3', 'e' => '33', 'f' => '333',
  'g' => '4', 'h' => '44', 'i' => '444',
  'j' => '5', 'k' => '55', 'l' => '555',
  'm' => '6', 'n' => '66', 'o' => '666',
  'p' => '7', 'q' => '77', 'r' => '777', 's' => '7777',
  't' => '8', 'u' => '88', 'v' => '888',
  'w' => '9', 'x' => '99', 'y' => '999', 'z' => '9999',
  ' ' => '*',
}

def pause(p, n)
  if KEYS[p][0] == KEYS[n][0] and KEYS[p] != '*'
    "(PAUSE)"
  else
    ""
  end
end

STDIN.each do |line|
  line.strip!.downcase!
  break if line == "*"
  print KEYS[line[0,1]]
  line.chars.each_cons(2) do |a,b|
    print pause(a, b)
    print KEYS[b]
  end
  puts
end

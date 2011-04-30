#!/usr/bin/env ruby

INFLATION = 1.03 ** 50

def newprice(x)
  (x * 100).round / 100
end

def round(x)
  ((x * 100).round / 100).prec_f
end

MENU = {
  'A' => ['Hamburger', 0.25],
  'B' => ['Cheeseburger', 0.30],
  'C' => ['Chili Dog', 0.35],
  'D' => ['Sub Sandwich', 0.65],
  'E' => ['Baked Pizza', 0.75],
  'F' => ['French Fries', 0.25],
  'G' => ['Pepsi-Cola', 0.25],
  'H' => ['Orange Soda', 0.15],
  'I' => ['Hot Coffee', 0.10],
  'J' => ['Milk', 0.15],
  'K' => ['Apple Pie', 0.30],
  'L' => ['Frosty Shake', 0.40],
  'M' => ['Popcorn', 0.15],
}

order = 1
total = 0
puts "ORDER #{order}"

STDIN.each do |line|
  n, i = line.split
  n = n.to_i
  if n == 0
    puts "ORDER #{order} TOTAL in 1957 = #{round(total)}"
    puts "ORDER #{order} TOTAL in 2007 - #{round(newprice(total))}"
    order += 1
    total = 0
    break if i == "Z"
    puts
    puts "ORDER #{order}"
  else
    item = MENU[i]
    puts "#{n} #{item[0]}"
    total += n * item[1]
  end
end

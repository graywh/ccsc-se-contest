#!/usr/bin/env ruby

def getOne(n)
    n % 10
end

def getTen(n)
    (n % 100) / 10
end

def getHund(n)
    n / 100
end

count = 1
File.readlines('prob5_in.txt').each_slice(2) do |act, line|
  act.strip!
  line.strip!
  print "Message #{count} (#{act}d): "
  case act
  when "encode"
    code = []
    0...line.length.each do |i|
      ch = line[i]
      code << getHund(ch) if ch > 99
      code << getTen(ch)
      code << getOne(ch)
    end
    print code.reverse
    puts
  when "decode"
    message = []
    line = line.chars.to_a.collect { |c| c.to_i }
    i = 0
    while i < line.length
      ch1 = line[i]
      ch2 = line[i+1]
      i += 2
      n = 10 * ch2 + ch1
      if n < 23
        n += 100
        i += 1
      end
      message << n.chr
    end
    print message.reverse
    puts
  end
  count += 1
end

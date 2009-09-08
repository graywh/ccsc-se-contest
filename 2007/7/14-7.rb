#!/usr/bin/env ruby

def same(a,b)
  return false if a.length != b.length
  a.each_index do |i|
    c = b[i..-1] + b[0...i]
    return true if a == c
    c.reverse!
    return true if a == c
  end
  return false
end

def min(x)
  m = x[0]
  x.each do |a|
    m = a if a < m
  end
  return m
end

def reorder(a)
  m = a.find_index min(a)
  a = a[m..-1] + a[0...m]
  if a[1] > a[-1]
    a.reverse!
    a = a[-1..-1] + a[0...-1]
  end
  return a
end

def find(conf, size, coll=Array.new(), arr=Array.new(), count=0)
  if arr.length == size and arr[0] != arr[-1]
    coll.each do |sarr|
      return [coll, count] if same([sarr], arr)
    end
    coll << arr.join('')
    puts coll[-1]
    return [coll, count+1]
  else
    ks = conf.keys.sort
    ks.each do |key|
      if arr.length == 0 or key != arr[-1] and conf[key] > 0
        conf[key] -= 1
        coll, count = find(conf, size, coll, arr + [key], count)
        conf[key] += 1
      end
    end
  end
  return [coll, count]
end

i = 1
while true
  l,c = STDIN.readline.split.collect { |x| x.to_i }
  break if l == 0 and c == 0
  puts if i > 1
  puts "Dataset #{i}:"
  config = {}
  l.times do |j|
    k = STDIN.readline.split
    config[k[0][0,1]] = k[1].to_i
  end
  coll, t = find(config, c)
  puts "Total number of possible seating arrangements = #{t}"
  i += 1
end

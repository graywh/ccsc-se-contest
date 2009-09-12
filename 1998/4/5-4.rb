#!/usr/bin/env ruby

CONV = {
  "B#" => "C",
  "C#" => "Db",
  "D#" => "Eb",
  "E#" => "F",
  "F#" => "Gb",
  "G#" => "Ab",
  "A#" => "Bb",
  "Bb" => "A#",
  "Cb" => "B",
  "Db" => "C#",
  "Eb" => "D#",
  "Fb" => "E",
  "Gb" => "F#",
  "Ab" => "G#"
}

INTERVAL = {
  "second"  => 1,
  "third"   => 2,
  "fourth"  => 3,
  "fifth"   => 4,
  "sixth"   => 5,
  "seventh" => 6,
  "octave"  => 0
}

NOTES = ["C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab", "A", "Bb", "B"]
CHANGE = [2, 2, 1, 2, 2, 2]

def sharp?(note)
   note[1] and note[1].chr == "#"
end

until STDIN.eof do
  keyn = STDIN.readline.strip
  line = STDIN.readline
  print "Key of #{keyn}: "
  keyn = CONV[keyn] if sharp?(keyn)
  i = 0
  i += 1 until NOTES[i] == keyn
  key = []
  key << NOTES[i]
  CHANGE.each do |j|
    i = (i + j) % 12
    key << NOTES[i]
  end
  until line.nil? or line.empty? do
    note, di, intrvl, line = line.split(nil, 4)
    print note
    sharp = sharp?(note) and keyn.length == 1
    note = CONV[note] if sharp
    i = 0
    valid = false
    while i < 7 and not valid do
      valid = (key[i] == note)
      i += 1
    end
    if valid
      intr = INTERVAL[intrvl]
      if di == "up"
        i = (i + intr - 1) % 7
      else
        i = (i - intr + 6) % 7
      end
      print ' ' + di + ' ' + intrvl + ' => '
      if sharp
        note = CONV[key[i]]
      else
        note = key[i]
      end
      if keyn.length == 1 and note[1]
        if note[1].chr == "#"
        print note
        else
          print CONV[note]
        end
      else
        print note
      end
    else
      print " is an invalid note for this key"
    end
    print '; ' if line and not line.empty?
  end
  puts
end

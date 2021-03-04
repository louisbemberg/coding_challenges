# GOAL: Write methods that can translate integer <=> roman numeral
# GIVEN: a Roman Numeral Dictionary

DICTIONARY = {
  "I" => 1,
  "IV" => 4,
  "V" => 5,
  "IX" => 9,
  "X" => 10,
  "XL" => 40,
  "L" => 50,
  "XC" => 90,
  "C" => 100,
  "CD" => 400,
  "D" => 500,
  "CM" => 900,
  "M" => 1000
}

def roman_to_integer(string)
  # TODO: TAKE A ROMAN NUMERAL STRING AND TURN IT INTO AN INTEGER
end

def integer_to_roman(integer)
  # TODO: TAKE AN INTEGER A TURN IT INTO A ROMAN NUMERAL STRING
end

# TESTS - RUN THE FILE TO GET FEEDBACK :)
puts "ROMAN_TO_INTEGER"
puts "#{"✅" if roman_to_integer("III") == 3} exp: 3 got: #{roman_to_integer("III")}"
puts "#{"✅" if roman_to_integer("IX") == 9} expected:9 got: #{roman_to_integer("IX")}"
puts "#{"✅" if roman_to_integer("DLXIV") == 564} expected:564 got: #{roman_to_integer("DLXIV")}"
puts "#{"✅" if roman_to_integer("CCXII") == 212} expected:212 got: #{roman_to_integer("CCXII")}"
puts "#{"✅" if roman_to_integer("CLVI") == 156} expected:156 got: #{roman_to_integer("CLVI")}"
puts "#{"✅" if roman_to_integer("CMXC") == 990} expected:990 got: #{roman_to_integer("CMXC")}"

puts
puts

puts "INTEGER_TO_ROMAN"
puts "#{"✅" if integer_to_roman(3) == "III"} expected:III got: #{integer_to_roman(3)}"
puts "#{"✅" if integer_to_roman(9) == "IX"} expected:IX got: #{integer_to_roman(9)}"
puts "#{"✅" if integer_to_roman(564) == "DLXIV"} expected:DLXIV got: #{integer_to_roman(564)}"
puts "#{"✅" if integer_to_roman(212) == "CCXII"} expected:CCXII got: #{integer_to_roman(212)}"
puts "#{"✅" if integer_to_roman(156) == "CLVI"} expected:CLVI got: #{integer_to_roman(156)}"
puts "#{"✅" if integer_to_roman(990) == "CMXC"} expected:CMXC got: #{integer_to_roman(990)}"

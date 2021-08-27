s = 'Python is an easy to learn powerful programming language It has efficient high-level data structures and a simple but effective approach to objectoriented programming Python elegant syntax and dynamic typing
'
t = 'programming Python elegant syntax and dynamic typing'

def missing_words(s, t)
  # split the strings into array of words:
  s_array = s.split
  t_array = t.split

  i = 0
  j = 0
  missing = []
  # we're going to look at every element in i
  until i == s_array.length - 1
    if s_array[i] == t_array[j]
      j += 1
    else
      missing << s_array[i]
    end
    i += 1
    puts "loop # #{i}, s-word is #{s_array[i]}, t-word is #{s_array[j]}"
  end
  missing
end

p missing_words(s, t)

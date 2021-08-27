require 'json'
require 'open-uri'

def count_words(url)
  document = {}

  begin
    text_serialized = URI.open(url).read
    text_convert = JSON.parse(text_serialized)
    p text_convert
    text = "#{text_convert['text']}"
    new_text = text.downcase.gsub(/[^a-z0-9\s]/i, '')
    words = new_text.split(' ')
    freq = Hash.new(0)
    words.each { |word| freq[word] += 1 }
    word_frequency = freq.sort.to_h
    sorted_word_frequency = word_frequency.sort_by { |word, count| count && word }.to_h
    p sorted_word_frequency.each { |word, count| document[word] = count }
    next_page_counter = count_words("#{text_convert['next_page']}")
    sorted_next_page_counter = next_page_counter.sort_by { |word, count| count && word }.to_h
    p sorted_next_page_counter.each { |word, count| document[word] = count }
  end while text_convert.has_key?("next_page")
  sorted_document = document.sort_by { |word, count| count && word }.to_h
  sorted_document.each { |word, count| puts "#{word}: #{count}" }
end
puts "What's the url that you want to process?"
url = gets.chomp
count_words(url)

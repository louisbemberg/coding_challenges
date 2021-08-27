# Every language has its own types of comments
# Ruby comments start with hashtags
# Other languages use <!--, !, //, etc.
# Write a method that gets rid of all comments of a string
# The method receives 2 arguments::
# 1) a string
# 2) an array containing the comment markers to check for
# example: comments("puts 'Hello World' # this is my fist line of code", ["#"])
require 'pry-byebug'
def comments(string, markers)
  markers_regex = "(#{markers.join('|')})"
  hashtag_regex = /(#{markers_regex}.*$)/
  scans = string.scan(hashtag_regex)
  output = string.dup
  scans.each do |s|
    output.gsub!(s[0], '')
  end
  output.split("\n").map(&:rstrip).join("\n")
end

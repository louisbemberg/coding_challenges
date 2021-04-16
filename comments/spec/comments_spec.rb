require_relative '../lib/comments_solution'

RSpec.describe '#comments' do
  it 'should remove comments from ruby code' do
    input = 'pi = 3.14 # declaring a variable'
    desired_output = 'pi = 3.14'
    expect(comments(input, ['#'])).to eq(desired_output)
  end

  it 'should remove comments from JS code' do
    input = 'const pi = 3.14 // declaring a variable'
    desired_output = 'const pi = 3.14'
    expect(comments(input, ['//'])).to eq(desired_output)
  end

  it 'should remove comments from JS *AND* Ruby code on different lines' do
    input = "const pi = 3.14 // declaring a variable in JS\npi = 3.1415 #declaring a variable in ruby"
    desired_output = "const pi = 3.14\npi = 3.1415"
    expect(comments(input, ['//', '#'])).to eq(desired_output)
  end

  it 'should keep the string intact if no comments' do
    input = 'const pi = 3.1415'
    desired_output = 'const pi = 3.1415'
    expect(comments(input, ['//', '#'])).to eq(desired_output)
  end

  it 'should keep the string intact if no comments, but with line jumps' do
    input = "const pi = 3.14\nconst e = mc^2"
    desired_output = "const pi = 3.14\nconst e = mc^2"
    expect(comments(input, ['//', '#'])).to eq(desired_output)
  end

  it 'should recognize what is a comment and what is not' do
    input = 'HelloWorld#HelloWorld'
    desired_output = 'HelloWorld'
    expect(comments(input, ['//', '#'])).to eq (desired_output)
  end
end


puts "TEST 3 - JS and Ruby comments on different lines:"
puts "result:"
puts comments("const pi = 3.14 // declaring a variable\npi = 3.1415 #declaring a variable in ruby", ['//', '#'])
puts "expected:"
puts "const pi = 3.14\npi = 3.1415"
puts

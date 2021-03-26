require_relative '../lib/anagrams'

RSpec.describe '#anagrams' do
  it 'should find anagrams of abba' do
    expect(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])).to eq(['aabb', 'bbaa'])
  end

  it 'should find anagrams of Hola' do
    expect(anagrams('Hola', ['Halo', 'Hello', 'Bonjour'])).to eq(['Halo'])
  end

  it 'should return an empty array if no anagrams found' do
    expect(anagrams('Mango', ['Pear', 'Apple'])).to eq([])
  end
end

# puts "got: #{anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])} expected: ['aabb', 'bbaa']"
# puts "got: #{anagrams('Hola', ['Halo', 'Hello', 'Bonjour'])} expected: ['Halo']"
# puts "got: #{anagrams('Mango', ['Pear', 'Apple'])} expected: []"

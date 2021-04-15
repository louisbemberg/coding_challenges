require_relative '../lib/snails_solution'

RSpec.describe '#snail' do
  it 'should return an ordered array of digits for a 4x4 matrix' do
    test_array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    expect(snail_recursive(test_array)).to eq((1..16).to_a)
  end

  it 'should return an ordered array of digits for a 3x3 matrix' do
    test_array = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    expect(snail_recursive(test_array)).to eq((1..9).to_a)
  end

  it 'should return an ordered array of digits for a 2x2 matrix' do
    test_array = [[1, 2], [4, 3]]
    expect(snail_recursive(test_array)).to eq((1..4).to_a)
  end

  it 'should return an empty array if an empty matrix was given' do
    test_array = []
    expect(snail_recursive(test_array)).to eq([])
  end
end

require_relative '../lib/color_conversions'

RSpec.describe '#rgb_to_hex' do
  it 'returns FFFFFF when receiving 255 255 255' do
    expect(rgb_to_hex(255, 255, 255)).to eq('FFFFFF')
  end

  it 'returns FFFFFF when receiving 255, 999, 300' do
    expect(rgb_to_hex(255, 999, 300)).to eq('FFFFFF')
  end

  it 'returns 000000 when receiving 0, 0, 0' do
    expect(rgb_to_hex(0, 0, 0)).to eq('000000')
  end

  it 'returns 000000 when receiving -30, 0, 0' do
    expect(rgb_to_hex(-30, 0, 0)).to eq('000000')
  end

  it 'returns 36474D when receiving 54, 71, 77' do
    expect(rgb_to_hex(54, 71, 77)).to eq('36474D')
  end

  it 'returns A30B73 when receiving 0, 0, 0' do
    expect(rgb_to_hex(163, 11, 115)).to eq('A30B73')
  end

  it 'returns 118573 when receiving 0, 0, 0' do
    expect(rgb_to_hex(17, 133, 115)).to eq('118573')
  end

end

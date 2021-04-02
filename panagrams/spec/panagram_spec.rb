require_relative '../lib/panagram.rb'

RSpec.describe '#panagram?' do
  describe 'Hello World' do
    it 'should not be a panagram' do
      expect(panagram?(subject)).to eq(false)
    end
  end

  describe 'empty String "" ' do
    it 'should not be a panagram' do
      subject = ''
      expect(panagram?(subject)).to eq(false)
    end
  end

  describe 'a_ab^^b0c56cddeeff_g, ghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz' do
    it 'should be a panagram' do
      expect(panagram?(subject)).to eq(true)
    end
  end

  describe 'the quick brown fox jumps over the lazy dog' do
    it 'should be a panagram' do
      expect(panagram?(subject)).to eq(true)
    end
  end

  describe 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z' do
    it 'should not be case sensitive and recognize the panagram' do
      expect(panagram?(subject)).to eq(true)
    end
  end
end

# Simplifying multilinear polynomials

poly = "-a+5ab+3a-c-2a"
poly2 = "a+5ba+3a-c-2a"
poly3 = '+8zb+11bz+13zbd-1zb+9zb+2bz+8bzd+1zdb-11b'
poly4 = "-abc+3a+2ac"
poly5 = "xyz+byz+by+xz"

def simplify(poly)
  # separating items per binomial
  full_elements = poly.scan(/([-+]*\d*)(\w+)/)
  # rearranging letters so that xca becomes acx
  full_elements.map! { |e| [e[0], e[1].chars.sort.join] }
  # sorting with priority 1: size, priority 2: alphabetical
  full_elements.sort_by! { |e| e[1].downcase }.sort_by! { |e| e[1].size }
  sums = {}
  full_elements.each do |element|
    if element[0] == "+" || element[0] == ""
      factor = 1
    elsif element[0] == "-"
      factor = -1
    else
      factor = element[0].to_i
    end
    binomial = element[1]
    sums[binomial] ? sums[binomial] += factor : sums[binomial] = factor
  end
  sums = sums.map do |e|
    e.reverse.join
  end
  # remove 0 factors:
  simplified = sums.reject { |s| s.start_with?('0') }
  p simplified
  simplified.map! do |s|
    # if there is a +1 or -1, turn it into nothing or -
    if s.match(/[-+]1\D+/)
      s[0..1] = s[0] == '-' ? '-' : ''
    end
    if s.match(/^1\D+/)
      s[0] = ''
    end
    s
  end
  simplified.join('+').gsub('+-', '-')
end

p simplify(poly)
p simplify(poly2)
p simplify(poly3)
p simplify(poly4)
p simplify(poly5)

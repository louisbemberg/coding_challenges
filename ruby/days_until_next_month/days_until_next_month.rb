require 'date'
def days_until_next_month(start_date)
  next_month = (start_date.month + 1) % 12
  next_first = Date.new(next_month == 1 ? start_date.year + 1 : start_date.year, next_month, 1)
  (next_first - start_date).to_i
end

puts days_until_next_month(Date.new(2021, 12, 24))
puts days_until_next_month(Date.new(2021, 1, 1))
puts days_until_next_month(Date.new(2021, 12, 31))
puts days_until_next_month(Date.new(2021, 2, 20))

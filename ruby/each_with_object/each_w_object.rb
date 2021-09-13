# data
options = { 'Max' => '54', 'Min' => '32' }
merged_options = { class: ' --ad', data: {} }

# objective:
{ "Max" => { :class => " --ad", :data => {}, :value => "54"},
 "Min" => { :class=>" --ad", :data => {}, :value => "32"}}

input_options = options.each_with_object({}) do |(k, v), hash|
  # puts "-----"
  # puts "k is #{k}, v is #{v}, hash is #{hash}"
  # puts "merged_options is #{merged_options}"
  hash[k] = merged_options.dup()
  # puts "hash[k] is #{hash[k]}"
  hash[k][:value] = v
  # puts "hash[k] is #{hash[k]}"
  # puts "hash[k][:value] is #{hash[k][:value]}"
  # puts "****"
end

p input_options

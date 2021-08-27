# We all know and love our CSS colors.
# We typically use 2 color codes: RGB and Hex
# Example of RGB: rgb(255, 0, 0) -red
# Example of RGB: rgb(0, 255, 0) -green
# Example of RGB: rgb(0, 0, 255) -blue
# Equivalent in HEX: #FF0000 -red
# Equivalent in HEX: #00FF00 -green
# Equivalent in HEX: #0000FF -blue

# Write a method that converts rgb into HEX.
# Rules:
# The method Receives 3 parameters, outputs a string
# Parameters should only range from 0-255.
# ^ In case values outside of that range, interpret as nearest possible
def rgb_to_hex(r, g, b)
end

# TESTS
# run 'rspec' to run the tests
# alternatively, you can play around with the code below:
p rgb_to_hex(255, 255, 255) # returns FFFFFF
p rgb_to_hex(255, 999, 300) # returns FFFFFF
p rgb_to_hex(0, 0, 0) # returns 000000
p rgb_to_hex(-30, 0, 0) # returns 000000
p rgb_to_hex(54, 71, 77) # returns #36474D
p rgb_to_hex(163, 11, 115) # returns  #A30B73
p rgb_to_hex(17, 133, 115) # returns 118573

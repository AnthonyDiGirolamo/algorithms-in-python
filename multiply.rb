#!/usr/bin/env ruby

require 'rubygems'
require 'byebug'
require 'pp'

def sum_numbers(one, two)
  carry = 0
  three = []
  i = one.size - 1
  j = two.size - 1
  while i >= 0 || j >= 0 do
    d = ((i >= 0 ? one[i] : 0) +
         (j >= 0 ? two[j] : 0)).to_i
    ones_place = (d % 10).to_i + carry
    carry      = (d / 10).to_i
    three.unshift(ones_place)
    i -= 1
    j -= 1
  end
  return three
end

def multiply_numbers(n1, n2)
  if n1.size < n2.size
    longer_number  = n2
    shorter_number = n1
  else
    longer_number  = n1
    shorter_number = n2
  end
  numbers_to_add = []

  pp longer_number
  pp shorter_number

  shorter_number.to_enum.with_index.reverse_each do |bottom_number, bottom_number_index|
    numbers_to_add << []
    carry = 0
    current_decimal_place = shorter_number.size - bottom_number_index - 1
    current_decimal_place.times do
      numbers_to_add.last << 0
    end
    longer_number.to_enum.with_index.reverse_each do |top_number, top_number_index|
      top_number_index
      d = (bottom_number *
           top_number).to_i
      ones_place = (d % 10).to_i + carry
      carry      = (d / 10).to_i
      numbers_to_add.last.unshift(ones_place)
    end
    numbers_to_add.last.unshift(carry) if carry > 0
  end
  pp numbers_to_add

  n3 = numbers_to_add.shift
  numbers_to_add.each do |number|
    n3 = sum_numbers(n3, number)
  end
  return n3
end


a =  "123".split('').collect(&:to_i)
b = "4321".split('').collect(&:to_i)
pp a
pp b
pp 123*4321
pp sum_numbers(a, b)

#     4321
#    * 123
#    -----
#    12963
#    86420
# + 432100
# --------
#   531483

pp multiply_numbers(a, b)

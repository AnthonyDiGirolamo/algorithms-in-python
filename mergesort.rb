#!/usr/bin/env ruby

require 'pry-byebug'
require 'pp'

module Blank
  refine Object do
    def blank?
      self.respond_to?(:empty?) ? empty? : !self
    end
    def present?
      !blank?
    end
  end
end

using Blank

def merge(left, right)
  result = []
  puts "merging: [#{left.join(',')}] and [#{right.join(',')}]"
  while left.present? || right.present?
    if left.present? && right.present?
      if left.first <= right.first
        result << left.shift
      else
        result << right.shift
      end
    elsif left.present?
      result << left.shift
    elsif right.present?
      result << right.shift
    end
  end
  puts "merged result:"
  pp result
  return result
end

def mergesort(a)
  p "called mergesort on: #{a.join(',')}"
  return a if a.size == 1
  midpoint = a.size/2
  left = a[0..midpoint-1] if midpoint-1 >= 0
  puts "left coords:"
  pp a[0..midpoint-1]
  pp a[0,midpoint]
  puts "left: #{left.join(',')}"
  right = a[midpoint..a.size-1] if a.size-1 >= midpoint
  puts "right coords:"
  pp a[midpoint..a.size-1]
  pp a[midpoint,a.size]
  puts "right: #{right.join(',')}"
  left = mergesort(left)
  right = mergesort(right)
  return merge(left, right)
end

a = [4, 6, 8, 3, 5667, 333, 7,
     8, 5, 2, 6, 8, 0, 9, 8]
mergesort a

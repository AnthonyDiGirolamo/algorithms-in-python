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
  return result
end

def mergesort(a)
  return a if a.size == 1
  midpoint = a.size/2
  left = a[0,midpoint]
  right = a[midpoint,a.size]
  left = mergesort(left)
  right = mergesort(right)
  return merge(left, right)
end

a = [4, 6, 8, 3, 5667, 333, 7,
     8, 5, 2, 6, 8, 0, 9, 8]
mergesort a

# [0, 2, 3, 4, 5, 6, 6, 7, 8, 8, 8, 8, 9, 333, 5667]

#!/usr/bin/env ruby
require 'rubygems'
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

class BSTNode
  attr_accessor :left, :right, :data
  def initialize(data = nil)
    self.data = data
  end

  def <<(data) insert(data) end

  def insert(data)
    self.data = data and return self if self.data.blank?
    node = self
    new_node = BSTNode.new(data)
    while node.present?
      previous = node
      if data < node.data
        node = node.left
      else
        node = node.right
      end
    end
    if data < previous.data
      previous.left = new_node
    else
      previous.right = new_node
    end
    return self
  end

  def pre_order
    return to_enum(:pre_order) unless block_given?

    yield data
    left.pre_order{|e| yield e} if left.present?
    right.pre_order{|e| yield e} if right.present?
  end

  def in_order
    return to_enum(:in_order) unless block_given?

    left.in_order{|e| yield e} if left.present?
    yield data
    right.in_order{|e| yield e} if right.present?
  end

  def print_tree(depth = 0)
    # same as in-order traversal but with a depth
    s = ""
    s += left.print_tree(depth+1) if left.present?
    s += "    "*depth + data.to_s + "\n"
    s += right.print_tree(depth+1) if right.present?
    return s
  end

  def data_and_depth(depth = 0)
    return to_enum(:data_and_depth, depth) unless block_given?
    left.data_and_depth(depth+1) {|e| yield e} if left.present?
    right.data_and_depth(depth+1) {|e| yield e} if right.present?
    yield [depth, data]
  end

  def depth_arrays
    data_and_depth.each_with_object({}) do |(depth, data), h|
      h[depth] ||= []
      h[depth] << data
      # pp depth
      # pp data
      # pp h
    end #.sort.collect{|(depth,list)| list} # if you want just the arrays in order
  end
end

bst = BSTNode.new('m') << 'd' << 'x' << 'w' << 'z' << 'a' << 'e'

pp bst.in_order.collect{|e| e.upcase}
pp bst.pre_order.collect{|e| e.upcase}

puts bst.print_tree

pp bst.depth_arrays

class BinarySearchTree
  def self.from_array(a)
    bst = BSTNode.new
    partition(a) do |element|
      bst.insert element
    end
    return bst
  end

  def self.partition(source_array)
    return to_enum(:partition, source_array) unless block_given?
    # p 'source_array'
    # pp source_array
    midpoint = source_array.size/2
    # p 'midpoint'
    # pp [midpoint, source_array[midpoint]]
    left  = source_array[0..midpoint-1] if midpoint-1 >= 0
    # p 'left'
    # pp [0, midpoint-1]
    # pp left
    right = source_array[midpoint+1..source_array.size-1] if source_array.size-1 >= midpoint+1
    # p 'right'
    # pp [midpoint+1, source_array.size-1]
    # pp right
    # puts ''
    yield source_array[midpoint]
    partition(left){|e| yield e}  if left.present?
    partition(right){|e| yield e} if right.present?
  end
end

a = %w(m d x w z a e).sort
# b = BinarySearchTree.partition(a).collect{|e| e}
# pp b
puts BinarySearchTree.from_array(a).print_tree

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
  attr_accessor :left, :right, :parent, :data
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
    new_node.parent = previous
    if data < previous.data
      previous.left = new_node
    else
      previous.right = new_node
    end
    return self
  end

  def pre_order
    return to_enum(:pre_order) unless block_given?

    yield self
    left.pre_order{|e| yield e} if left.present?
    right.pre_order{|e| yield e} if right.present?
  end

  def in_order
    return to_enum(:in_order) unless block_given?

    left.in_order{|e| yield e} if left.present?
    yield self
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
    left.data_and_depth(depth+1)  {|e| yield e} if left.present?
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
    end
  end

  def root_node
    root = self
    while root.parent.present?
      root = root.parent
    end
    return root
  end

  def next_in_order
    last_node = nil
    root_node.in_order do |node|
      return node if last_node == self
      last_node = node
    end
    return false
  end
end

bst = BSTNode.new('m') << 'd' << 'x' << 'w' << 'z' << 'a' << 'e' << '0' << 'b'

pp bst.in_order.collect{|e| e.data.upcase}
pp bst.pre_order.collect{|e| e.data.upcase}

puts bst.print_tree
pp bst.left.left.left.next_in_order.data
pp bst.right.right.next_in_order

depth_elements = bst.depth_arrays
pp depth_elements
# if you want just the arrays in order
# pp depth_elements.sort.collect{|(depth,list)| list}
# pp depth_elements.sort_by { |k, v| k }.collect(&:last)
pp depth_elements.sort.collect(&:last)

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

  def self.common_ancestors(a, b)
    found = false
    a.pre_order.each do |child_of_a|
      found = true and break if child_of_a == b
    end
    return a if found

    n = a
    while !found
      found = true and break if n.parent.blank?
      prev_node = n
      n = n.parent
      direction = n.left == prev_node ? :right : :left
      sub_tree_root = n.send(direction)
      if sub_tree_root.present?
        sub_tree_root.pre_order do |sub_node|
          found = true and break if sub_node == b
        end
      end
    end
    return n if found
    return false
  end
end

a = %w(m d x w z a e 0 b).sort
b = BinarySearchTree.partition(a).collect{|e| e}
pp b
puts BinarySearchTree.from_array(a).print_tree

bst = BSTNode.new('m') << 'd' << 'x' << 'w' << 'z' << 'a' << 'e' << '0' << 'b'
puts bst.print_tree

d = bst.left
b = bst.left.left.right
pp d == BinarySearchTree.common_ancestors(d, b)

w = bst.right.left
e = bst.left.right
pp bst == BinarySearchTree.common_ancestors(w, d)
pp d == BinarySearchTree.common_ancestors(e, b)

#!/Users/anthony/.rbenv/shims/ruby
require 'rubygems'
require 'pry-byebug'
require 'pp'

require_relative 'blank'
using Blank

class Node
  attr_accessor :links, :data

  def initialize(data)
    self.links = []
    self.data = data
  end

  def to_s
    self.data.to_s
  end

  def is_connected_to?(end_point)
    return true if end_point == self
    start_point = self
    current_nodes = [self]
    while !current_nodes.empty?
      current_nodes = current_nodes.each_with_object([]) do |node, new_current_nodes|
        node.links.each do |new_node|
          return true if new_node == end_point
          new_current_nodes << new_node if new_node != start_point
        end
      end
    end
    return false
  end
end

a = Node.new('a')
b = Node.new('b')
c = Node.new('c')
d = Node.new('d')
e = Node.new('e')
f = Node.new('f')
z = Node.new('z')

a.links << b
a.links << c
b.links << d
b.links << e
e.links << f
c.links << f
f.links << z
# z.links << a

p a.is_connected_to?(a)
p a.is_connected_to?(b)
p a.is_connected_to?(z)
p e.is_connected_to?(b)

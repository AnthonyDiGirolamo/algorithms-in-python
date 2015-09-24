#!/usr/bin/env ruby

class Object
  def blank?
    respond_to?(:empty?) ? !!empty? : !self
  end

  def present?
    !blank?
  end
end

class Node
  attr_accessor :data, :next

  def initialize(data)
    self.data = data
  end

  def tail
    node = self
    while node.next.present?
      node = node.next
    end
    return node
  end

  def append_to_tail(d)
    tail.next = Node.new(d)
  end

  def <<(d)
    append_to_tail(d)
  end

  def to_s
    self.data.to_s
  end

  def loop_start
    visited = {}
    n = self
    while n.next.present? do
      key = n.object_id
      return n if visited.has_key?(key)
      visited[key] = true
      n = n.next
    end
    return false
  end

  def loop_start_using_two_pointers
    a = b = self
    while b.present? && b.next.present? do
      a = a.next
      b = b.next.next
      break if a == b
    end
    return false if a.blank? || b.blank?
    a = self
    while a != b do
      a = a.next
      b = b.next
    end
    return b
  end
end

h = Node.new('a')
h << 'b' << 'c' << 'd' << 'e' << 'f'

node = h
puts h.data
while node.next.present?
  node = node.next
  puts node.data
end

h.tail.next = h.next.next

puts h.loop_start
puts h.loop_start_using_two_pointers

l = Node.new('a')
l << 'b' << 'c' << 'd' << 'e' << 'f'
puts l.loop_start_using_two_pointers

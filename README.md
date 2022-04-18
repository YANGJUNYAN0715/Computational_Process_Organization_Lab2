# GROUP: 123456 - lab 1 - variant 1

Author:
Junyan Yang(1310204834@qq.com)
Haodong Guo(guohaodong@hdu.edu.cn)

## Project structure

- `unrolled_linked_list.py` -- implementation of `UnrolledLinkedList` 
class with `hello` and `add` features. Stateless.

- `unrolled_linked_list_test.py` -- unit and PBT tests for `UnrolledLinkedList`.

## Features

- PBT: `test_default_node_capacity`
- PBT: `test_custom_node_capacity`
- PBT: `test_empty`
- PBT: `test_delete_item`
- PBT: `test_get_item`
- PBT: `test_set_item`
- PBT: `test_iteration`
- PBT: `test_len`
- PBT: `test_contains`
- PBT: `test_variable`
- PBT: `test_variable`
- PBT: `test_to_list`
- PBT: `test_from_list`


## Contribution
Junyan Yang(1310204834@qq.com) -- writes the main code of this lab

​Donghao Guo(guohaodong@hdu.edu.cn) -- runs the tests.

## Changelog

- 14.04.2022 - 0
  - Initial

## Design notes

An unrolled linked list is a linear data structure that is a variant on the linked list. 
Instead of just storing 1 element at each node, unrolled linked lists store an entire array at each node.

​So we design this structure, it can realize the function of delitem, getitem, setitem, iter, 
str, len, reverse, contains, append. We set the max_node_capacity as 4, 
which means that the number of array elements of node should be from half of max_node_capacity to max_node_capacity, 
if using  function of  delitem or append, we should care about this and vary it. 
Thinking about one situation,  the tail(type is node) has an array of 4 elements, if we append a new element, 
then it will exceed the limitation, therefore we will add a new node, 
set the tail.next as the new node and set this new node as tail, 
then put the former node's last half  elements into the new tail node and put the new appending element as well, 
it will make the balance, 
that's an example about the thinking of function of appending, well getitem, 
setitem and other functions are easier to design.


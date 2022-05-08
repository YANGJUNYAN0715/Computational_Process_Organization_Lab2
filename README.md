# GROUP: 123456 - lab 2 - variant 1

Author:

Junyan Yang(1310204834@qq.com)

Haodong Guo(guohaodong@hdu.edu.cn)

## Project structure

- `unrolled_linked_list.py` -- implementation of `UnrolledLinkedList`

class with `hello` and `add` features. Stateless.

- `unrolled_linked_list_test.py` -- unit and tests for

`UnrolledLinkedList`.

## Features

- test: `test_immutable`
- PBT test: `test_from_list`
- PBT test: `test_cons`
- PBT test: `test_to_list`
- PBT test: `test_size`
- test: `test_find`
- PBT test: `test_filter`
- test: `test_len`
- test: `test_map`
- test: `test_reduce`
- test: `test_remove`
- PBT test: `test_concat`
- PBT test: `test_monoid_identity`
- PBT test: `test_monoid_associativity`
- test: `test_add_to_tail`

## Contribution

Junyan Yang(1310204834@qq.com) -- check the code grammar

Donghao Guo(guohaodong@hdu.edu.cn) -- writes the main code of this lab

## Changelog

- 08.05.2022 - 0
  - Initial

## Design notes

An unrolled linked list is a linear data structure
that is a variant on the linked list.
Instead of just storing 1 element at each node,
unrolled linked lists store an entire array at each node.

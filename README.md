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

- PBT test: test_default_node_capacity
- PBT test: test_custom_node_capacity
- PBT test: test_empty
- PBT test: test_delete_item
- PBT test: test_get_item
- PBT test: test_set_item
- PBT test: test_iteration
- PBT test: test_len
- PBT test: test_member
- PBT test: test_variable
- PBT test: test_to_list
- PBT test: test_from_list
- test: test_filter
- PBT test: test_concat
- test: test_empty_function
- PBT test: test_reduce

## Contribution

Junyan Yang(1310204834@qq.com) -- writes the main code of this lab

Donghao Guo(guohaodong@hdu.edu.cn) -- runs the test

## Changelog

- 08.05.2022 - 0
  - Initial
- 09.05.2022 - 1
  - Change the data structure into immutable type
- 09.05.2022 - 2
  - Add analysis and conclusion in README.md
- 27.05.2022 - 3
  - Use the test API provided
  - Modify some functions
- 28.05.2022 - 4
  - Add functions of map and filter
- 08.06.2022 - 5
  - Add docstrings for all functions and also type hints

## Design notes

An unrolled linked list is a linear data structure
that is a variant on the linked list.
Instead of just storing 1 element at each node,
unrolled linked lists store an entire array at each node.

## Analysis and conclusion

An immutable implementation can prevent the structure from being modified
by different threads, but the disadvantage is that it adds difficulties in
designing the structure which seems to be verbose.
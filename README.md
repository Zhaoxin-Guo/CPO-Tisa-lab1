# Tisa-lab1-variant1

This repo is the Lab1 of Computational Process Organization in ITMO, 2022 spring.

## Variant

* 1 - Unrolled linked list

## Laboratory work description

* You can use the built-in list inside nodes
* You need to check that your implementation correctly works with None value
* A user should specify node size
* You need to implement functions/methods for getting/setting value by index

## Project structure description

* `Mutable.py` -- implementation of `UnrolledLinkedList`
 class with `size`,`set`,`remove`,`get`and other features.

* `MutableTest.py` -- unit and PBT tests for `Mutable`.

## Contribution

* Chen Biao(1377681089@qq.com)
  * Implement the `mutable.py`
  * Write `README.md`
  * Source code framework construction

* Guo Zhaoxin(zhaoxin_guo@163.com)
  * Implement the `mutableTest.py`
  * Write `README.md`
  * Created GitHub repository

## Features

`set(idx, obj)`: setting value by index

`remove(idx)`: remove value by index

`size()`: Return the size of unrolled linked list

`is_member(member)`: Return a boolean indicating whether
the element is a member of the unrolled linked list

`from_list(list)`: Conversion from list

`to_list`: Conversion to list

`get(idx)`: get value by index

`filter()`: Filter data structure by specific predicate

`map()`: Map elements of the unrolled linked list by specific function

`reduce()`: Process elements of the unrolled linked list
to build a return value by specific function

`__iter__()`: Implementation an iterator in Python style

`__next__()`: Implementation an iterator in Python style

PBT: `test_from_list_to_list_equality`,`test_python_len_and_list_size_equality`

## Changelog

* 20.4.2022- 11
  * Chen Biao updated `mutable.py`.
* 20.4.2022- 10
  * Guo Zhaoxin updated `mutableTest.py`.
* 14.4.2022- 9
  * Chen Biao add `requirements.txt`.
  * Add `check.yml`
  * Updated `README.md`.
* 14.4.2022- 8
  * Guo Zhaoxin updated `mutableTest.py`.
  * Testing `iterator`feature.
  * Updated `README.md`.
* 14.4.2022- 7
  * Chen Biao updated `mutable.py`.
  * Implementing `iterator`feature.
  * Updated `README.md`. Add Implementation restrictions.
* 13.4.2022 - 6
  * Guo Zhaoxin updated `mutableTest.py`.
  * Testing `is_member(member)`,`filter()`,`map()`and`reduce()`features.
  * Updated `README.md`. Add Design notes.
* 13.4.2022 - 5
  * Chen Biao updated `mutable.py`.
  * Implementing `is_member(member)`,`filter()`,`map()`and`reduce()` features.
  * Updated `README.md`.
* 13.4.2022 - 4
  * Guo zhaoxin upload `mutableTest.py`.
  * Testing some features.
* 13.4.2022 - 3
  * Chen Biao upload `mutable.py`.
  * Implementing some features.
* 13.4.2022 - 2
  * Chen Biao updated `README.md`. Add Project structure description and Features.
* 13.4.2022 - 1
  * Guo Zhaoxin updated `README.md`.
* 13.4.2022 - 0
  * Initial.

## Design notes

### Implementation restrictions

The capacity of unrolled linked list is manually set and cannot be customized.

### Advantages and disadvantages of unittest

* Advantages：
  * Support automated testing
  * Secondary development is convenient
  * Organize test cases together by class
* Disadvantages：
  * Must be written in TestCase subclass
  * Must write test method
  * Difficult to expand

### Advantages and disadvantages of PBT tests

* Advantages：
  * Check with automatically generated input data to ensure enough test cases
  * Allows developers to increase test coverage and effectively save time
* Disadvantages：
  * Not covering all examples

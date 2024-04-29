#  This file is part of Pynguin.
#
#  SPDX-FileCopyrightText: 2019–2024 Pynguin Contributors
#
#  SPDX-License-Identifier: MIT
#

# Automatically generated by Pynguin.
import pytest
import queue_example as module_0


def test_case_0():
    int_0 = 1256
    queue_0 = module_0.Queue(int_0)
    assert (
        f"{type(queue_0).__module__}.{type(queue_0).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_0.max == 1256
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 1256
    bool_0 = queue_0.full()
    assert bool_0 is False


def test_case_1():
    int_0 = -2944
    with pytest.raises(AssertionError):
        module_0.Queue(int_0)


def test_case_2():
    int_0 = -726
    int_1 = 2505
    queue_0 = module_0.Queue(int_1)
    assert (
        f"{type(queue_0).__module__}.{type(queue_0).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_0.max == 2505
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 2505
    bool_0 = queue_0.enqueue(int_0)
    assert bool_0 is True
    assert queue_0.tail == 1
    assert queue_0.size == 1
    with pytest.raises(AssertionError):
        module_0.Queue(int_0)


def test_case_3():
    int_0 = 2423
    queue_0 = module_0.Queue(int_0)
    assert (
        f"{type(queue_0).__module__}.{type(queue_0).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_0.max == 2423
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 2423
    queue_0.dequeue()
    bool_0 = queue_0.full()
    assert bool_0 is False
    with pytest.raises(AssertionError):
        module_0.Queue(bool_0)


def test_case_4():
    int_0 = 1001
    queue_0 = module_0.Queue(int_0)
    assert (
        f"{type(queue_0).__module__}.{type(queue_0).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_0.max == 1001
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 1001
    int_1 = 649
    queue_1 = module_0.Queue(int_1)
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    int_2 = 3263
    queue_2 = module_0.Queue(int_2)
    assert queue_2.head == 0
    assert queue_2.tail == 0
    assert queue_2.size == 0
    bool_0 = queue_2.full()
    assert bool_0 is False
    int_3 = 2010
    bool_1 = queue_1.enqueue(int_3)
    assert bool_1 is True
    assert queue_1.tail == 1
    assert queue_1.size == 1
    int_4 = queue_1.dequeue()
    assert int_4 == 2010
    assert queue_1.head == 1
    assert queue_1.size == 0
    bool_2 = queue_0.full()
    assert bool_2 is False
    bool_3 = queue_1.full()
    assert bool_3 is False
    bool_4 = queue_1.enqueue(int_3)
    assert bool_4 is True
    assert queue_1.tail == 2
    assert queue_1.size == 1
    queue_2.dequeue()


def test_case_5():
    int_0 = 1235
    queue_0 = module_0.Queue(int_0)
    assert (
        f"{type(queue_0).__module__}.{type(queue_0).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_0.max == 1235
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 1235
    queue_1 = module_0.Queue(int_0)
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    bool_0 = queue_1.empty()
    assert bool_0 is False
    int_1 = 4904
    int_2 = 3504
    bool_1 = queue_0.empty()
    assert bool_1 is False
    queue_2 = module_0.Queue(int_2)
    assert queue_2.head == 0
    assert queue_2.tail == 0
    assert queue_2.size == 0
    bool_2 = queue_2.enqueue(int_1)
    assert bool_2 is True
    assert queue_2.tail == 1
    assert queue_2.size == 1


def test_case_6():
    int_0 = 1187
    queue_0 = module_0.Queue(int_0)
    assert (
        f"{type(queue_0).__module__}.{type(queue_0).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_0.max == 1187
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 1187
    bool_0 = queue_0.empty()
    assert bool_0 is False
    bool_1 = queue_0.enqueue(int_0)
    assert bool_1 is True
    assert queue_0.tail == 1
    assert queue_0.size == 1
    queue_1 = module_0.Queue(bool_1)
    assert (
        f"{type(queue_1).__module__}.{type(queue_1).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_1.max is True
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    assert (
        f"{type(queue_1.data).__module__}.{type(queue_1.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_1.data) == 1
    bool_2 = queue_1.full()
    assert bool_2 is False
    int_1 = 1441
    bool_3 = queue_1.enqueue(int_1)
    assert bool_3 is True
    assert queue_1.size == 1
    bool_4 = queue_1.full()
    assert bool_4 is True
    int_2 = 1080
    queue_2 = module_0.Queue(int_2)
    assert queue_2.head == 0
    assert queue_2.size == 0
    bool_5 = queue_1.full()
    assert bool_5 is True
    queue_3 = module_0.Queue(bool_5)
    assert (
        f"{type(queue_3).__module__}.{type(queue_3).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_3.max is True
    assert queue_3.head == 0
    assert queue_3.tail == 0
    assert queue_3.size == 0
    assert (
        f"{type(queue_3.data).__module__}.{type(queue_3.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_3.data) == 1
    bool_6 = queue_3.empty()
    assert bool_6 is False
    queue_1.enqueue(bool_2)
    bool_8 = queue_1.empty()
    assert bool_8 is True
    queue_2.dequeue()
    queue_3.dequeue()
    queue_4 = module_0.Queue(bool_4)
    assert queue_4.head == 0
    assert queue_4.size == 0
    bool_9 = queue_4.empty()
    assert bool_9 is False
    int_3 = 2245
    bool_10 = queue_2.empty()
    assert bool_10 is False
    bool_11 = queue_3.empty()
    assert bool_11 is False
    queue_0.full()
    queue_5 = module_0.Queue(int_3)
    assert queue_5.head == 0
    assert queue_5.size == 0
    int_4 = queue_0.dequeue()
    assert int_4 == 1187
    assert queue_0.head == 1
    assert queue_0.size == 0
    bool_13 = queue_3.empty()
    assert bool_13 is False
    queue_4.dequeue()
    int_5 = 481
    queue_6 = module_0.Queue(int_5)
    assert queue_6.head == 0
    assert queue_6.size == 0
    queue_3.dequeue()
    queue_6.enqueue(bool_4)
    assert queue_6.tail == 1
    assert queue_6.size == 1
    queue_3.dequeue()
    bool_15 = queue_0.empty()
    assert bool_15 is False
    queue_3.full()


def test_case_7():
    int_0 = 1187
    queue_0 = module_0.Queue(int_0)
    assert (
        f"{type(queue_0).__module__}.{type(queue_0).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_0.max == 1187
    assert queue_0.head == 0
    assert queue_0.tail == 0
    assert queue_0.size == 0
    assert (
        f"{type(queue_0.data).__module__}.{type(queue_0.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_0.data) == 1187
    bool_0 = queue_0.empty()
    assert bool_0 is False
    bool_1 = queue_0.enqueue(int_0)
    assert bool_1 is True
    assert queue_0.tail == 1
    assert queue_0.size == 1
    queue_1 = module_0.Queue(bool_1)
    assert (
        f"{type(queue_1).__module__}.{type(queue_1).__qualname__}"
        == "queue_example.Queue"
    )
    assert queue_1.max is True
    assert queue_1.head == 0
    assert queue_1.tail == 0
    assert queue_1.size == 0
    assert (
        f"{type(queue_1.data).__module__}.{type(queue_1.data).__qualname__}"
        == "array.array"
    )
    assert len(queue_1.data) == 1
    bool_2 = queue_1.full()
    assert bool_2 is False
    int_1 = 1441
    bool_3 = queue_1.enqueue(int_1)
    assert bool_3 is True
    assert queue_1.size == 1
    bool_4 = queue_1.full()
    assert bool_4 is True
    int_2 = 1080
    queue_2 = module_0.Queue(int_2)
    assert queue_2.head == 0
    assert queue_2.size == 0
    int_3 = queue_1.dequeue()
    assert int_3 == 1441
    assert queue_1.size == 0
    int_4 = queue_0.dequeue()
    assert int_4 == 1187
    assert queue_0.head == 1
    assert queue_0.size == 0
    bool_5 = queue_2.full()
    assert bool_5 is False
    bool_6 = queue_1.enqueue(bool_0)
    assert bool_6 is True
    assert queue_1.size == 1
    int_5 = -30
    with pytest.raises(AssertionError):
        module_0.Queue(int_5)

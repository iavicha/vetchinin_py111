"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any
COUNT_PRIORITY = 11
priority_deque = {p: [] for p in range(COUNT_PRIORITY)}
print(priority_deque)

def enqueue(elem: Any, priority: int = 0) -> None:

    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global priority_deque
    print(priority_deque)
    priority_deque.fromkeys(elem, priority)
    print(priority_deque)
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_deque
    priority_deque.clear()

    return None

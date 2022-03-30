## Simple implementation of LRU Cache in Python

No library/modules are used, just built-in standard Python `dict` and `Class`

Since an LRU Cache require fast look-up and fast insertion and deletion, the LRU Cache is basically an almagamation of a doubly linked-list and a hashtable(`dict`)

Doubly Linked-List
| Time Complexity | Space Complexity |
| --------------- | ---------------- |
| Insertion: O(1) | O(n)             |
| Deletion: O(1)  |                  |

- *node deletion is O(1) since we already know its location, prev & next due to the hashtable*

Hashtable
| Time Complexity | Space Complexity |
| --------------- | ---------------- |
| Insertion: O(1) | O(n)             |
| Deletion: O(1)  |                  |
| Searching: O(1) |                  |

- *the value stored in the hashtable will be the node object and it will be accessed by the key. Node removal is cheap since we will have the node's prev and next*



# 28. Find the Index of the First Occurrence in a String

## Problem Description

Given two strings `haystack` and `needle`, return the index of the first occurrence of `needle` in `haystack`, or -1 if `needle` is not part of `haystack`.

### Example 1:

**Input:**
```python
haystack = "sadbutsad"
needle = "sad"
```

**Output:**
```python
0
```

**Explanation:**
"sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

### Example 2:

**Input:**
```python
haystack = "leetcode"
needle = "leeto"
```

**Output:**
```python
-1
```

**Explanation:**
"leeto" did not occur in "leetcode", so we return -1.

## Constraints

- `1 <= haystack.length, needle.length <= 10^4`
- `haystack` and `needle` consist of only lowercase English characters.
.

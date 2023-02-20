# 651. 4 Keys Keyboard

> Medium

------

Imagine you have a special keyboard with the following keys:

- <kbd>A</kbd>: Print one `'A'` on the screen.
- <kbd>Ctrl</kbd> + <kbd>A</kbd>: Select the whole screen.
- <kbd>Ctrl</kbd> + <kbd>C</kbd>: Copy selection to buffer.
- <kbd>Ctrl</kbd> + <kbd>V</kbd>: Print buffer on screen appending it after what has already been printed.

Given an integer `n`, return the maximum number of `'A'` you can print on the screen with at most `n` presses on the keys.

**Example 1:**

```
Input: n = 3
Output: 3
Explanation: We can at most get 3 A's on screen by pressing the following key sequence:
A, A, A
```

**Example 2:**

```
Input: n = 7
Output: 9
Explanation: We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl+A, Ctrl+C, Ctrl+V, Ctrl+V
```
# 212. Word Search II


class Solution:
    # Backtracking with Trie
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        WORD_KEY = '$'

        # Build a trie.
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            # Mark the existence of a word in trie node.
            node[WORD_KEY] = word

        matched_words = []

        def backtrack(i: int, j: int, parent: dict) -> None:
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            letter = board[i][j]
            if letter not in parent:
                return

            curr_node = parent[letter]

            # Remove the matched word to avoid duplicates.
            matched_word = curr_node.pop(WORD_KEY, False)
            if matched_word:
                matched_words.append(matched_word)

            # Mark the cell as visited.
            board[i][j] = "#"

            # Explore the neighbors.
            for row_offset, col_offset in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                next_i, next_j = i + row_offset, j + col_offset
                backtrack(next_i, next_j, curr_node)

            board[i][j] = letter

            # Optimization: incrementally remove the matched leaf node in the trie.
            # For a leaf node in Trie, once we traverse it (i.e. find a matched word), we would no longer need to traverse it again.
            if not curr_node:
                parent.pop(letter)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    backtrack(i, j, trie)
        return matched_words
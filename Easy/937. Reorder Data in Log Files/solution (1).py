# 937. Reorder Data in Log Files


class Solution:
    # Sorting by Keys
    def reorderLogFiles(self, logs: list[str]) -> list[str]:

        def get_key(log: list[str]) -> tuple:
            id, content = log.split(" ", maxsplit=1)
            return (0, content, id) if content[0].isalpha() else (1, None, None)

        return sorted(logs, key=get_key)
# 1244. Design a Leaderboard

> Medium

------

Design a `Leaderboard` class, which has three functions:

- `addScore(playerId, score)` updates the leaderboard by adding `score` to the given player's score. If there is no player with such id in the leaderboard, add him to the leaderboard with the given `score`.
- `top(K)` returns the score sum of the top `K` players.
- `reset(playerId)` resets the score of the player with the given id to `0` (in other words erase it from the leaderboard). It is guaranteed that the player was added to the leaderboard before calling this function.

Initially, the leaderboard is empty.

**Example:**

```
Input:
["Leaderboard","addScore","addScore","addScore","addScore","addScore","top","reset","reset","addScore","top"]
[[],[1,73],[2,56],[3,39],[4,51],[5,4],[1],[1],[2],[2,51],[3]]
Output:
[null,null,null,null,null,null,73,null,null,null,141]

Explanation:
Leaderboard leaderboard = new Leaderboard ();
leaderboard.addScore(1,73);     // leaderboard = [[1,73]];
leaderboard.addScore(2,56);     // leaderboard = [[1,73],[2,56]];
leaderboard.addScore(3,39);     // leaderboard = [[1,73],[2,56],[3,39]];
leaderboard.addScore(4,51);     // leaderboard = [[1,73],[2,56],[3,39],[4,51]];
leaderboard.addScore(5,4);      // leaderboard = [[1,73],[2,56],[3,39],[4,51],[5,4]];
leaderboard.top(1);             // returns 73;
leaderboard.reset(1);           // leaderboard = [[2,56],[3,39],[4,51],[5,4]];
leaderboard.reset(2);           // leaderboard = [[3,39],[4,51],[5,4]];
leaderboard.addScore(2,51);     // leaderboard = [[2,51],[3,39],[4,51],[5,4]];
leaderboard.top(3);             // returns 141 = 51 + 51 + 39;
```
// 1244. Design a Leaderboard


class Leaderboard {

    private Map<Integer, Integer> scores;

    private TreeMap<Integer, Integer> sortedScores;

    public Leaderboard() {
        this.scores = new HashMap<Integer, Integer>();
        this.sortedScores = new TreeMap<>(Collections.reverseOrder());
    }

    public void addScore(int playerId, int score) {
        // The scores dictionary simply contains the mapping from the `playerId` to their score.
        // The sortedScores contain a BST with key as the score and value as the number of players that have that score.
        if (!this.scores.containsKey(playerId)) {
            this.scores.put(playerId, score);
            this.sortedScores.put(score, this.sortedScores.getOrDefault(score, 0) + 1);

        } else {
            // Since the current player's score is changing, we need to update the sortedScores map to reduce count for the old score.
            int preScore = this.scores.get(playerId);
            int playerCount = this.sortedScores.get(preScore);

            // If no player has this score, remove it from the tree.
            if (playerCount == 1) {
                this.sortedScores.remove(preScore);
            } else {
                this.sortedScores.put(preScore, playerCount - 1);
            }

            // Updated score.
            int newScore = preScore + score;
            this.scores.put(playerId, newScore);
            this.sortedScores.put(newScore, this.sortedScores.getOrDefault(newScore, 0) + 1);
        }
    }

    public int top(int K) {

        int count = 0;
        int sum = 0;

        // In-order traversal over the scores in the TreeMap.
        for (Map.Entry<Integer, Integer> entry: this.sortedScores.entrySet()) {

            // Number of players that have this score.
            int times = entry.getValue();
            int key = entry.getKey();

            for (int i = 0; i < times; i++) {
                sum += key;
                count++;

                // Found top-K scores, break.
                if (count == K) {
                    break;
                }
            }

            // Found top-K scores, break.
            if (count == K) {
                break;
            }
        }

        return sum;
    }

    public void reset(int playerId) {
        int preScore = this.scores.get(playerId);
        this.sortedScores.put(preScore, this.sortedScores.get(preScore) - 1);
        if (this.sortedScores.get(preScore) == 0) {
            this.sortedScores.remove(preScore);
        }

        this.scores.remove(playerId);
    }
}
// 721. Accounts Merge

// Runtime: 29 ms, faster than 87.22% of Java online submissions for Accounts Merge.

// Memory Usage: 46 MB, less than 54.36% of Java online submissions for Accounts Merge.


// Depth-First Search
class Solution {

    HashSet<String> visited = new HashSet<>();

    Map<String, List<String>> adjacent = new HashMap<String, List<String>>();

    private void dfs(List<String> mergedAccount, String email) {
        visited.add(email);

        // Add the email vector that contains the current component's emails.
        mergedAccount.add(email);

        if (!adjacent.containsKey(email)) {
            return;
        }

        for (String neighbor : adjacent.get(email)) {
            if (!visited.contains(neighbor)) {
                dfs(mergedAccount, neighbor);
            }
        }
    }

    public List<List<String>> accountsMerge(List<List<String>> accountList) {
        for (List<String> account : accountList) {

            // Building adjacency list.
            // Adding edge between first email to all other emails in the account.
            String firstEmail = account.get(1);
            for (int i = 2; i < account.size(); i++) {
                String email = account.get(i);

                if (!adjacent.containsKey(firstEmail)) {
                    adjacent.put(firstEmail, new ArrayList<String>());
                }

                adjacent.get(firstEmail).add(email);

                if (!adjacent.containsKey(email)) {
                    adjacent.put(email, new ArrayList<String>());
                }

                adjacent.get(email).add(firstEmail);
            }
        }

        // Traverse over all accounts to store components.
        List<List<String>> mergedAccounts = new ArrayList<>();

        for (List<String> account : accountList) {
            String name = account.get(0);
            String firstEmail = account.get(1);

            // If email is visited, then it's a part of different component.
            // Hence perform DFS only if email is not visited yet.
            if (!visited.contains(firstEmail)) {
                List<String> mergedAccount = new ArrayList<>();
                // Adding account name at the 0-th index.
                mergedAccount.add(name);

                dfs(mergedAccount, firstEmail);
                Collections.sort(mergedAccount.subList(1, mergedAccount.size()));
                mergedAccounts.add(mergedAccount);
            }
        }

        return mergedAccounts;
    }
}
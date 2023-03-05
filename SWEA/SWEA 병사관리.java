public class UserSolution_copy {
    class Team {
        Node head[];
        Node tail[];

        public Team() {
            head = new Node[MAX_SCORE + 1];
            tail = new Node[MAX_SCORE + 1];
        }
    }
    class Node {
        int idx;
        int version;
        Node nxt;
        public Node() {}
        public Node(int idx, int version) {
            this.idx = idx;
            this.version = version;
            this.nxt = null;
        }
    }
    int version[], team[];
    Team teams[];
    final int MAX_ID = 1000000;
    final int MAX_TEAM = 5;
    final int MAX_SCORE = 5;

    public void init() {
        teams = new Team[MAX_TEAM + 1];
        for (int i=1; i<=MAX_TEAM; i++) {
            teams[i] = new Team();

            for (int j=1; j<=MAX_SCORE; j++) {
                Node node = new Node(0, 0);
                teams[i].head[j] = teams[i].tail[j] = node;
            }
        }

        version = new int[MAX_ID + 1];
        team = new int[MAX_ID + 1];
    }

    public Node getNode(int idx) {
        Node node = new Node(idx, ++version[idx]);
        return node;
    }
    public void hire(int mID, int mTeam, int mScore) {
        Node node = getNode(mID);
        teams[mTeam].tail[mScore].nxt = node;
        teams[mTeam].tail[mScore] = node;

        team[mID] = mTeam;
    }
    public void fire(int mID) {
        version[mID] = -1; // disable 처리
    }
    public void updateSoldier(int mID, int mScore) {
        hire(mID, team[mID], mScore);
    }
    public void updateTeam(int mTeam, int mChangeScore) {
        if (mChangeScore < 0) {
            for (int i=1; i<=MAX_SCORE; i++) {
                int k = i + mChangeScore;
                k = k < 1 ? 1 : k;

                // !! 옮기고 나서 다시 지워벼리지 않게 주의
                if (k == i) continue;

                // !! teams == null인 경우
                if (teams[mTeam].head[i].nxt == null) continue;
                teams[mTeam].tail[k].nxt = teams[mTeam].head[i].nxt;
                teams[mTeam].tail[k] = teams[mTeam].tail[i];

                teams[mTeam].head[i].nxt = null;
                teams[mTeam].tail[i] = teams[mTeam].head[i];
            }
        }
        if (mChangeScore > 0) {
            for (int i=MAX_SCORE; i>=1; i--) {
                int k = i + mChangeScore;
                k = k > 5 ? 5 : k;

                if (k == i) continue;

                if (teams[mTeam].head[i].nxt == null) continue;
                teams[mTeam].tail[k].nxt = teams[mTeam].head[i].nxt;
                teams[mTeam].tail[k] = teams[mTeam].tail[i];

                teams[mTeam].head[i].nxt = null;
                teams[mTeam].tail[i] = teams[mTeam].head[i];
            }
        }
    }
    public int bestSoldier(int mTeam) {
        for (int i=MAX_SCORE; i>=1; i--) {
            Node node = teams[mTeam].head[i];
            if (node == null) continue;
            int idx = 0;
            while (node != null) {
                if (node.version == version[node.idx]) {
                    idx = node.idx > idx ? node.idx : idx;
                }
                node = node.nxt;
            }
            if (idx != 0)
                return idx;
        }
        return 0;
    }
}

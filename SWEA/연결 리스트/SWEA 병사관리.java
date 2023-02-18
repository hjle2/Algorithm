class UserSolution
{
    class Node {
        int id;
        int v;
        Node nxt;

        public Node() {
        }
        public Node(int id, int v) {
            this.id = id;
            this.v = v;
            nxt = null;
        }
    }
    class Team {
        Node[] head = new Node[6];
        Node[] tail = new Node[6];
    }

    int solderTeam[];
    int solderVersion[];

    Team teams[];

    public Node getNode(int id) {
        if (id == 0) {
            return new Node(id, 0);
        }
        Node newNode = new Node(id, ++solderVersion[id]);
        return newNode;
    }
    public void init()
    {
        solderTeam = new int[100001];
        solderVersion = new int[100001];

        teams = new Team[6];
        for (int i=1; i<6; i++) {
            teams[i] = new Team();

            for (int j=1; j<6; j++) {
                Node node = getNode(0);
                teams[i].head[j] = teams[i].tail[j] = node;
            }
        }
    }

    public void hire(int mID, int mTeam, int mScore)
    {
        Node node = getNode(mID);
        teams[mTeam].tail[mScore].nxt = node;
        teams[mTeam].tail[mScore] = node;
        solderTeam[mID] = mTeam;
    }

    public void fire(int mID)
    {
        solderVersion[mID] = -1;
    }

    public void updateSoldier(int mID, int mScore)
    {
        int team = solderTeam[mID];
        Node node = getNode(mID);
        teams[team].tail[mScore].nxt = node;
        teams[team].tail[mScore] = node;
    }

    public void updateTeam(int mTeam, int mChangeScore)
    {
        if (mChangeScore > 0) {
            for (int i=5; i>0; i--) {

                int k = i + mChangeScore;
                k = k > 5 ? 5 : k;

                if (i == k) continue;

                if (teams[mTeam].head[i].nxt == null) continue;
                teams[mTeam].tail[k].nxt = teams[mTeam].head[i].nxt;
                teams[mTeam].tail[k] = teams[mTeam].tail[i];

                teams[mTeam].head[i].nxt = null;
                teams[mTeam].tail[i] = teams[mTeam].head[i];
            }
        }

        if (mChangeScore < 0) {
            for (int i=1; i<=5; i++) {

                int k = i + mChangeScore;
                k = k < 1 ? 1 : k;

                if (i == k) continue;

                if (teams[mTeam].head[i].nxt == null) continue;
                teams[mTeam].tail[k].nxt = teams[mTeam].head[i].nxt;
                teams[mTeam].tail[k] = teams[mTeam].tail[i];

                teams[mTeam].head[i].nxt = null;
                teams[mTeam].tail[i] = teams[mTeam].head[i];
            }

        }
    }

    public int bestSoldier(int mTeam)
    {
        for (int i=5; i>0; i--) { // 점수 순서대로 순회
            Node node = teams[mTeam].head[i].nxt;
            if (node == null) continue;
            int ans = 0;
            while (node != null) {
                if (node.v == solderVersion[node.id]) {
                    ans = node.id > ans ? node.id : ans;
                }
                node = node.nxt;
            }

            if (ans != 0) return ans;
        }
        return 0;
    }
}

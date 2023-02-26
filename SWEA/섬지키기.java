// 구조물에 대한 규칙을 찾아야 한다
// 구조물은 오르쪽 구조물에서 왼쪽 구조물의 높이를 빼준다.
// 격자에 대해서는 왼쪽에서 오른쪽 값을 빼준다.
// -> 각 차이는 같은 값이 나온다
// 이 값을 미리 계산해 둔다. (전처리)

import java.util.*;

class UserSolution {
    public final int MAX_N = 20;
    public final int MAX_HASH = 9999;

    public int n;
    public int[][] initMap = new int[MAX_N + 2][MAX_N + 2];
    public int[][] modifiedMap = new int[MAX_N + 2][MAX_N + 2];

    public class Candidate {
        int r;
        int c;
        boolean isHorizontal;
        boolean isReverse;

        public Candidate(int r, int c, boolean isHorizontal, boolean isReverse) {
            this.r = r;
            this.c = c;
            this.isHorizontal = isHorizontal;
            this.isReverse = isReverse;
        }
    }

    public Map<Integer, List<Candidate>> map;

    public void addCandidate(int hash, int r, int c, boolean isHorizon, boolean isReverse) {
        Candidate candidate = new Candidate(r, c, isHorizon, isReverse);
        if (map.containsKey(hash)) {
            map.get(hash).add(candidate);
        } else {
            List<Candidate> list = new ArrayList<>();
            list.add(candidate);
            map.put(hash, list);
        }
    }
    public int getCandidateSize(int hash) {
        if (map.containsKey(hash)) {
            return map.get(hash).size();
        } else {
            return 0;
        }
    }
    public List<Candidate> getCandidateList(int hash) {
        if (map.containsKey(hash)) {
            return map.get(hash);
        } else {
            return new ArrayList<>();
        }
    }
    public void init(int N, int[][] mMap) {
        n = N;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                modifiedMap[i + 1][j + 1] = initMap[i + 1][j + 1] = mMap[i][j];
        map = new HashMap<>();
        // >> 전처리 모든 길이 L 구조물에 대한 HASH값 구하기
        // 각 자리의 차이를 숫자로 나타내어 해시값으로 이용한다
        // 2~5(최대 구조물의 길이)
        for (int length = 2; length <= 5; length++) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j + length - 1 <= n; j++) {
                    int hash = 0;
                    for (int k = 0; k + 1 < length; k++)
                        hash = hash * 10 + (initMap[i][j + k + 1] - initMap[i][j + k] + 5);
//                    candidate[hash].add(new Candidate(i, j, true, false));
                    addCandidate(hash, i, j, true, false);

                    int reverseHash = 0;
                    for (int k = length - 1; k - 1 >= 0; k--)
                        reverseHash = reverseHash * 10 + (initMap[i][j + k - 1] - initMap[i][j + k] + 5);

                    if (reverseHash != hash) // 대칭 키 중복 저장을 방지하기 위해서
                        addCandidate(reverseHash, i, j, true, true);
//                        candidate[reverseHash].add(new Candidate(i, j, true, true));
                }
            }
            // >>

            for (int i = 1; i + length - 1 <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    int hash = 0;
                    for (int k = 0; k + 1 < length; k++)
                        hash = hash * 10 + (initMap[i + k + 1][j] - initMap[i + k][j] + 5);
                    addCandidate(hash, i, j, false, false);

                    int reverseHash = 0;
                    for (int k = length - 1; k - 1 >= 0; k--)
                        reverseHash = reverseHash * 10 + (initMap[i + k - 1][j] - initMap[i + k][j] + 5);
                    if (reverseHash != hash)
                        addCandidate(reverseHash, i, j, false, true);
                }
            }
        }
    }

    public int numberOfCandidate(int M, int[] mStructure) {
        if (M == 1)
            return n * n;

        // 음수를 방지하기 위해서 섬의 고도의 최대 높이 5인 5를 더해준다
        // 1~5이기 때문에 높이 차이의 최소 값은 -4가 되는데 +4를 하게되면 08과 8이 구분이 되지 않는다
        // +6을 하게 되면 높이 차이의 값이 10이 될 수 있기 떄문에 딱 5만 가능하다
        int hash = 0;
        for (int i = 0; i + 1 < M; i++)
            hash = hash * 10 + (mStructure[i] - mStructure[i + 1] + 5);
        return getCandidateSize(hash);
    }

    public int[] dx = {1, 0, -1, 0};
    public int[] dy = {0, 1, 0, -1};

    public int unsubmergedArea(int[][] mMap, int mSeaLevel) {
        boolean check[][] = new boolean[MAX_N + 2][MAX_N + 2];
        Queue<int[]> q = new LinkedList<>();
        for (int i = 0; i <= n + 1; i++) {
            for (int j = 0; j <= n + 1; j++) {
                // 테두리 바다인 부분에서 시작한다
                if (i == 0 || i == n + 1 || j == 0 || j == n + 1) {
                    q.add(new int[]{i, j});
                    check[i][j] = true;
                } else
                    check[i][j] = false;
            }
        }
        while (!q.isEmpty()) {
            int[] front = q.poll();
            for (int i = 0; i < 4; i++) {
                int[] rear = {front[0] + dx[i], front[1] + dy[i]};

                // 격자 범위 내고, 방문하지 않은 땅,
                if (rear[0] >= 1 && rear[0] <= n && rear[1] >= 1 && rear[1] <= n) {
                    if (!check[rear[0]][rear[1]] && mMap[rear[0]][rear[1]] < mSeaLevel) {
                        q.add(rear);
                        check[rear[0]][rear[1]] = true;
                    }
                }
            }
        }
        int ret = 0;
        for (int i = 1; i <= n; i++)
            for (int j = 1; j <= n; j++)
                if (!check[i][j])
                    ret++;
        return ret;
    }

    public int maxArea(int M, int[] mStructure, int mSeaLevel) {
        int ret = -1;
        if (M == 1) {
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= n; j++) {
                    modifiedMap[i][j] = initMap[i][j] + mStructure[0];
                    ret = Math.max(ret, unsubmergedArea(modifiedMap, mSeaLevel));
                    modifiedMap[i][j] = initMap[i][j];
                }
            }
            return ret;
        }

        int hash = 0;
        for (int i = 0; i + 1 < M; i++)
            hash = hash * 10 + (mStructure[i] - mStructure[i + 1] + 5);

        for (Candidate wall : getCandidateList(hash)) {
            if (wall.isHorizontal) {
                int height = mStructure[0] + (wall.isReverse ? initMap[wall.r][wall.c + M - 1] : initMap[wall.r][wall.c]);
                for (int i = 0; i < M; i++)
                    modifiedMap[wall.r][wall.c + i] = height; // 구조물 설치

                ret = Math.max(ret, unsubmergedArea(modifiedMap, mSeaLevel));

                for (int i = 0; i < M; i++)
                    modifiedMap[wall.r][wall.c + i] = initMap[wall.r][wall.c + i]; // 구조물 제거
            } else {
                int height = mStructure[0] + (wall.isReverse ? initMap[wall.r + M - 1][wall.c] : initMap[wall.r][wall.c]);
                for (int i = 0; i < M; i++)
                    modifiedMap[wall.r + i][wall.c] = height;
                ret = Math.max(ret, unsubmergedArea(modifiedMap, mSeaLevel));
                for (int i = 0; i < M; i++)
                    modifiedMap[wall.r + i][wall.c] = initMap[wall.r + i][wall.c];
            }
        }
        return ret;
    }
}

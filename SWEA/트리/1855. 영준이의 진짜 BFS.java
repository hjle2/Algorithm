import java.io.*;
import java.util.*;

public class Solution {
    static int N;
    static ArrayList<Integer>[] graph;
    static int[][] par;
    static int[] d;

    static int DEPTH;

    public static void init() {
        graph = new ArrayList[N+1];
        for (int i = 0; i < N+1; i++) {
            graph[i] = new ArrayList<>();
        }
        par = new int[N+1][DEPTH];
        d = new int[N+1];
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int TC = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= TC; ++tc) {
            N = Integer.parseInt(br.readLine()); // 노드의 갯수
            DEPTH = (int) (Math.log(N) / Math.log(2)) + 2; // 트리의 깊이
            init();
            int k;
            par[1][0] = 0; // root 노드의 부모는 0
            d[1] = 0; // root 노드의 깊이는 0

            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 2; i <= N; i++) {
                k = Integer.parseInt(st.nextToken()); // i의 부모노드 k
                graph[k].add(i); // k의 자식노드에 i추가
                par[i][0] = k; // i의 부모는 k임을 저장
                d[i] = d[k] + 1; // i의 깊이는 부모 노드의 깊이 + 1
            }
            for (int y = 1; y < DEPTH; y++) {
                for (int x = 1; x <= N; x++) {
                    par[x][y] = par[par[x][y - 1]][y - 1]; // par[x][0]은 x노드의 부모 노드 par[x][1] 은 par[x]노드의 부모의 부모
                }
            }
            bw.write("#" + tc + " " + bfs() + "\n");
        }
        bw.flush();
        bw.close();
    }

    public static int LCA(int x, int y) { // 최소 공통 부모 찾기
        if (d[x] > d[y]) {
            int tmp = x;
            x = y;
            y = tmp;
        }

        if (par[y][0] == x) { // x가 y의 부모라면 거리는 1
            return 1;
        }

        int len = 0;
        // 같은 높이까지 노드 이동시키기
        while (d[x] != d[y]) {
            x = par[x][0];
            len++;
        }

        // 같은 높이일 경우 공통 부모까지 하나씩 올리기
        while (x != y) {
            x = par[x][0];
            y = par[y][0];
            len += 2;
        }
        return len;
    }

    public static int LCA(int x, int y, int cnt) { // 최소 공통 부모 찾기
        if (d[x] > d[y]) {
            int tmp = x;
            x = y;
            y = tmp;
        }

        if (par[y][0] == x) { // x가 y의 부모라면 거리는 1
            return 1;
        }
        for (int i = DEPTH -1; i >= 0; i--) { // 같은 높이까지 노드 이동시키기
            if (d[y] - d[x] >= (1 << i)) {
                y = par[y][i];
                cnt += (1 << i);
            }
        }
        if (par[y][0] != par[x][0]) { // 같은 높이일 경우 공통 부모까지 하나씩 올리기
            for (int i = DEPTH -1; i >= 0; i--) {
                if (par[x][i] != par[y][i]) {
                    cnt += 2 * (1 << i);
                    x = par[x][i];
                    y = par[y][i];
                }
            }
        }
        if (par[x][0] == par[y][0]) { // 부모가 같다면
            return cnt + 2; // 왜 + 2,,?
        }
        return -1;
    }

    public static long bfs() {
        boolean[] visit = new boolean[100001];

        long result = 0;
        int pre;
        Queue<Integer> q = new LinkedList<>();
        q.offer(1); // root node 첫번째
        visit[1] = true;
        pre = 1; // 이전 노드

        while (!q.isEmpty()) {
            int cur = q.poll(); // 현재 노드
            for (int i = 0; i < graph[cur].size(); i++) {
                int child = graph[cur].get(i);

                if (visit[child]) continue;
                q.offer(child);
                visit[child] = true;
                result += LCA(pre, child, 0); // 현재 노드와 이전노드의 거리
                pre = child; // 이전 노드
            }
        }
        return result;
    }
}

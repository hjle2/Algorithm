import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution { // _3_파핑파핑 지뢰

    public static int solve() {
        int cnt = 0;
        for (int r=0; r<N; r++) {
            for (int c=0; c<N; c++) { // 모든 좌표를 순회하면서
                if (map[r][c] == '*') continue;
                if (!isZero(r, c)) continue; // 0이 아니라면 패스
                if (clicked[r][c]) continue; // 이미 클릭된 칸이면 패스
                // 0이면, 클릭
                cnt += click(r, c, 0);
            }
        }
        return maxClick - cnt;
    }
    // r, c 칸을 클릭해서 숫자로 표시되는 주변에 있는 칸의 갯수 cnt
    public static int click(int r, int c, int cnt) {
        int nr, nc;
        if (clicked[r][c]) --cnt; // 지금 칸이 이미 클릭되어 있으면 -1
        clicked[r][c] = true; // 클릭 처리

        for (int i=0; i<8; i++) { // 인접한 8칸을 탐색한다.
            nr = r + dx[i]; nc = c + dy[i]; // 탐색할 칸의 좌표
            if (!inRange(nr, nc)) continue; // 격자 범위 안에 없으면 패스
            if (clicked[nr][nc]) continue; // 이미 숫자로 표시된 좌표는 패스
            clicked[nr][nc] = true;
            if (isZero(nr, nc)) { // 숫자로 표시된 칸이 0이라면,
                cnt += click(nr, nc, 1);
            }
            ++cnt; // 뒤집은 주변 칸
        }
        if (cnt < 0) return 0;
        return cnt;
    }
    public static boolean isZero(int r, int c) {
        int nr, nc;
        for (int i=0; i<8; i++) { // 인접한 8면을 탐색한다.
            nr = r + dx[i];
            nc = c + dy[i];
            if (!inRange(nr, nc)) continue;
            if (map[nr][nc] == '*') return false; // 지뢰가 있다면 false
        }
        return true; // 주변 8칸에 지뢰가 없다면 0이 맞다.
    }

    public static List<int[]> getZeros() { // 0의 위치를 구하는 함수
        List<int[]> zeroList = new ArrayList<>();

        for (int r=0; r<N; r++) {
            for (int c = 0; c < N; c++) {
                boolean flag = true;
                if (map[r][c] == '*') continue; // 지뢰가 있는 칸은 제외
                for (int i = 0; i < 8; i++) { // 지뢰가 없는 칸 중에서 8방향 탐색

                    int nr = r + dx[i]; // 탐색할 좌표
                    int nc = c + dy[i];

                    if (!inRange(nr, nc)) continue; // 범위 밖은 제외

                    if (map[nr][nc] == '*') { // 주변에 지뢰가 하나라도 있다면 0이 아니기 때문에 그만 탐색한다.
                        flag = false;
                        break;
                    }
                }
                if (flag) { // 8방향에 지뢰가 없다면 해당 위치는 0!
                    zeroList.add(new int[]{r, c});
                }
            }
        }
        return zeroList;
    }
    public static int getMaxClick() {
        int cnt = 0;
        for (int r=0; r<N; r++) {
            for (int c=0; c<N; c++) {
                if (map[r][c] == '.') {
                    ++cnt;
                }
            }
        }
        return cnt;
    }
    public static boolean inRange(int r, int c) {
        return 0 <= r && r < N && 0 <= c && c < N;
    }
    static char[][] map; // 지뢰찾기 map
    static List<int[]> zeros; // zero의 위치 좌표
    static boolean[][] clicked;
    static int maxClick; // 최대 클릭 수
    static int N; // map의 크기
    static int[] dx = {0, 0, 1, 1, 1, -1, -1, -1};
    static int[] dy = {1, -1, -1, 0, 1, -1, 0, 1}; // 인점 8칸을 탐색하기 위한 dx, dy

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int TC = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= TC; tc++) {
            // map 초기화
            N = Integer.parseInt(br.readLine()); // 지뢰 찾기하는 표의 크기
            map = new char[N][N];
            clicked = new boolean[N][N];
            StringTokenizer st;
            for (int i=0; i<N; i++) {
                st = new StringTokenizer(br.readLine());
                map[i] = st.nextToken().toCharArray();
            }
            zeros = getZeros();
            maxClick = getMaxClick();

            bw.write("#" + tc + " " + solve() + "\n");
        }
        bw.flush();
        bw.close();
    }
}

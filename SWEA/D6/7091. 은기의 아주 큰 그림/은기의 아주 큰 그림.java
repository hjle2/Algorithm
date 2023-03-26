import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Solution {

    private static long[] dreamRowHash;
    private static long[][] teacherRowHash;

    private static int H, W; // 꿈에서 본 그림의 크기 -> 해시를 구할 격자의 크기
    private static long hash, power; // getRowHash 또는 getColumnHash할 때 갱신되고 그 다음 해시를 구하는 getRightHash에서 활용됨

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int T = Integer.parseInt(br.readLine());
        for (int testCase = 1; testCase <= T; testCase++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            H = Integer.parseInt(st.nextToken());
            W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int widthGap = M - W;
            int heightGap = N - H;

            // i행의 해시
            dreamRowHash = new long[H];
            for (int h = 0; h < H; h++) {
                dreamRowHash[h] = getRowHash(br.readLine());
            }
            // 전체 해시
            long dreamHash = getColumnHash(dreamRowHash);

            // 가로로 해시 구하기
            teacherRowHash = new long[N + 1][M + 1];
            for (int i = 0; i < N; i++) {
                String line = br.readLine();
                teacherRowHash[0][i] = getRowHash(line);

                for (int j = 0; j < widthGap; j++) {
                    teacherRowHash[j + 1][i] = getRightHash(line, j);
                }
            }

            // 세로로 해시 구하면서 꿈에서 본 그림이랑 비교하기
            int count = 0;
            for (int j = 0; j <= widthGap; j++) {
                if (dreamHash == getColumnHash(teacherRowHash[j])) {
                    count++;
                }

                for (int i = 0; i < heightGap; i++) {
                    if (dreamHash == getRightHash(j, i)) {
                        count++;
                    }
                }
            }

            sb.append("#").append(testCase).append(" ").append(count).append("\n");
        }
        System.out.print(sb);
    }

    private static long getRowHash(String line) {
        hash = 0;
        power = 1;
        for (int w = 0; w < W; w++) {
            hash += line.charAt(W - w - 1) * power; // ?1. 왜 뒤쪽부터 해쉬에 더해줘야 하는지..?
            if (w < W - 1) {
                power *= 33;
            }
        }

        return hash;
    }

    private static long getColumnHash(long[] rowHash) {
        hash = 0;
        power = 1;
        for (int h = 0; h < H; h++) {
            hash += rowHash[H - h - 1] * power;
            if (h < H - 1) {
                power *= 5381;
            }
        }

        return hash;
    }

    private static long getRightHash(String line, int prv) {
        hash -= line.charAt(prv) * power;
        return hash = hash * 33 + line.charAt(prv + W);
    }

    private static long getRightHash(int j, int i) {
        hash -= teacherRowHash[j][i] * power;
        return hash = hash * 5381 + teacherRowHash[j][i + H];
    }
}
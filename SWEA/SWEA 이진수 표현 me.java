import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    public static String solve(int N, int M) {
        // 마지막 N 개의 비트를 확인할 변수
        int bit = (1 << N) - 1;
        int result = bit & M;

        if (result == bit) {
            return "ON";
        }
        return "OFF";
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int TC = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= TC; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            bw.write("#" + tc + " " + solve(N, M) + "\n");
        }
        bw.flush();
        bw.close();
    }
}

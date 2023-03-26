import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int TC = Integer.parseInt(br.readLine());
        for (int tc=1; tc<=TC; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());

            bw.write("#" + tc + " " + solve(a, b, k) + "\n");
        }
        bw.flush();
        bw.close();
    }

    public static long solve(int a, int b, int k) {
        int sum = a + b;
        long ret = 1;
        long n = 2;
        while (k > 0) {
            if (k % 2 == 1) {
                ret = (ret * n) % sum;
            }
            n = (n * n) % sum;
            k /= 2;
        }
        return sum / 2 < ret * a % sum? sum - ret * a % sum : ret * a % sum;
    }
}
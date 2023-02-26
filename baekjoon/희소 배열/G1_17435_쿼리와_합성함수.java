import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int m = Integer.parseInt(br.readLine());
        int log = (int)(Math.log(m) / Math.log(2)) + 1;
        System.out.println(log);
        StringTokenizer st = new StringTokenizer(br.readLine());

        // generate table
        int dp[][] = new int[m + 1][log + 1];
        for (int i=1; i<=m; i++) {
            dp[i][0] = Integer.parseInt(st.nextToken());
        }

        // init table
        for (int y=1; y<=log; y++) {
            for (int x=1; x<=m; x++) {
                dp[x][y] = dp[dp[x][y-1]][y-1];
            }
        }

        // query
        int q = Integer.parseInt(br.readLine());
        for (int i=0; i<q; i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());

            for (int j=0; j<=log; j++) {
                if ((n & (1 << j)) > 0)
                    x = dp[x][j];
            }
            bw.write(x + "\n");
        }
        bw.flush();
        bw.close();
    }
}

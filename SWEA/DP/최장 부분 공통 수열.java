package _3주차;

import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    public static int solve(char s1[], char s2[]) {
        int l1 = s1.length + 1;
        int l2 = s2.length + 1;

        int dp[][] = new int[l1][l2];
        for (int i=0; i<l1; i++) {
            for (int j=0; j<l2; j++) {
                dp[i][j] = 0;
            }
        }

        for (int i=1; i<l1; i++) {
            for (int j=1; j<l2; j++) {
                if (s1[i-1] == s2[j-1]) {
                    dp[i][j] = Math.max(dp[i-1][j-1] + 1, dp[i-1][j]);
                } else {
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[l1-1][l2-1];
    }
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int TC = Integer.parseInt(br.readLine());
        for (int tc=1; tc<=TC; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String s1 = st.nextToken();
            String s2 = st.nextToken();

            bw.write("#" + tc + " " + solve(s1.toCharArray(), s2.toCharArray()) + "\n");
        }
        bw.flush();
        bw.close();
    }
}

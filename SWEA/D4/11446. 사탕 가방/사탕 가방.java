import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int T = Integer.parseInt(br.readLine());
        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int N = Integer.parseInt(st.nextToken());
            long M = Long.parseLong(st.nextToken());
            st = new StringTokenizer(br.readLine(), " ");
            Long[] candy = new Long[N];
            long max = Long.MIN_VALUE;
            for (int i = 0; i < N; i++) {
                candy[i] = Long.valueOf(st.nextToken());
                max = Math.max(max, candy[i]); // 가진 사탕 중 가장 많이 가진 사탕(종류)
            }

            long low = 1L;
            long high = max; // 가장 큰 수는 가장 많은 사탕의 갯수
            long ans = 0l;
            // 가방을 mid개만큼 만들 수 있을까?
            // -> 가방을 mid개 만들려면 각 가방에 최대 몇 개의 사탕을 넣을 수 있는지 계산
            while (low <= high) {
                long mid = (low + high) / 2;
                long sum = 0L;
                for (int i = 0; i < N; i++) {
                    sum += (candy[i] / mid);
                }
                // M개의 사탕이 들어갔을 때 가방의 갯수를 구한다
                if (sum < M) {
                    high = mid - 1;
                } else {
                    ans = mid;
                    low = mid + 1;
                }
            }
            bw.append("#" + tc + " " + ans + "\n");
        }
        bw.flush();
    }
}
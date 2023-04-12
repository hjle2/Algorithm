import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        // << init
        int n = Integer.parseInt(br.readLine());

        Gifticon gifticon[] = new Gifticon[n];
        for (int i=0; i<n; i++) {
            gifticon[i] = new Gifticon();
        }

        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            gifticon[i].left_day = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            gifticon[i].plan_day = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(gifticon);
        // >>

        int ans = 0;

        int prv_max = gifticon[0].plan_day;
        int cur_max = -1;

        for (int i=0; i<n; i++) {
            int left_day = gifticon[i].left_day;
            int plan_day = gifticon[i].plan_day;

            if (left_day < prv_max) {
                if (prv_max < plan_day) {
                    prv_max = plan_day;
                }
                int cnt = (prv_max - left_day + 29) / 30;
                left_day += cnt * 30;
                ans += cnt;
            }

            cur_max = Math.max(cur_max, left_day);

            if (i + 1 < n && gifticon[i].plan_day != gifticon[i+1].plan_day) {
                prv_max = cur_max;
            }
        }
        bw.write("" + ans);
        bw.flush();
        bw.close();
    }

    static class Gifticon implements Comparable {
        public int left_day;
        public int plan_day;

        @Override
        public int compareTo(Object o) {
            Gifticon a = (Gifticon) o;
            if (plan_day == a.plan_day) {
                return left_day - a.left_day;
            }
            return plan_day - a.plan_day;
        }
    }
}
//5
//10 20 30 40 50
//50 40 30 20 10
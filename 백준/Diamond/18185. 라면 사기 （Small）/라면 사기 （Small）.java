import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


        // << init
        int n = Integer.parseInt(br.readLine());

        int ar[] = new int[n+2];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            ar[i] = Integer.parseInt(st.nextToken());
        }
        // >>
        int ans = 0;

        for (int i=0; i<n; i++) {
            // 3 개 가능한 경우
            if (ar[i + 1] <= ar[i + 2]) {
                int min_ = Math.min(Math.min(ar[i], ar[i + 1]), ar[i + 2]);
                ans += 7 * min_;

                ar[i] -= min_;
                ar[i + 1] -= min_;
                ar[i + 2] -= min_;

                min_ = Math.min(ar[i], ar[i + 1]);
                ans += 5 * min_;

                ar[i] -= min_;
                ar[i + 1] -= min_;
            }
            // 불가능한 경우
            else {
                int min_ = Math.min(ar[i], ar[i + 1] - ar[i + 2]);
                ans += 5 * min_;

                ar[i] -= min_;
                ar[i + 1] -= min_;


                min_ = Math.min(Math.min(ar[i], ar[i + 1]), ar[i + 2]);
                ans += 7 * min_;

                ar[i] -= min_;
                ar[i + 1] -= min_;
                ar[i + 2] -= min_;
            }

            ans += ar[i] * 3;
        }
        bw.write("" + ans);
        bw.flush();
        bw.close();
    }
}
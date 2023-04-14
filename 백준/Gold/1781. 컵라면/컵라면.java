import java.io.*;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int n = Integer.parseInt(br.readLine());

        int cup[][] = new int[n][2];
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            cup[i][0] = Integer.parseInt(st.nextToken());
            cup[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(cup, (a, b) -> {
            if (a[0] == b[0]) return b[1] - a[1];
            return a[0] - b[0];
        });
        PriorityQueue<Integer> que = new PriorityQueue<>();

        for (int i=0; i<n; i++) {
            que.add(cup[i][1]);

            while (que.size() > cup[i][0]) {
                que.poll();
            }
        }
        int ans = 0;
        for (int s: que) {
            ans += s;
        }

        bw.write("" + ans);
        bw.flush();
        bw.close();
    }
}
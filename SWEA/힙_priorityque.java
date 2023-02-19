
import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Solution  {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int TC = Integer.parseInt(br.readLine());
        for (int tc=1; tc<=TC; tc++) {
            bw.write("#" + tc + " ");
            PriorityQueue<Integer> que = new PriorityQueue<>();

            int N = Integer.parseInt(br.readLine());
            for (int i=0; i<N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());

                if (Integer.parseInt(st.nextToken()) == 1) {
                    int x = Integer.parseInt(st.nextToken());
                    que.add(x);
                } else {
                    if (que.size() == 0) {
                        bw.write(-1 + " ");
                    } else {
                        bw.write(que.poll() + " ");
                    }
                }
            }
            bw.write("\n");
        }

        bw.flush();
        bw.close();
    }
}

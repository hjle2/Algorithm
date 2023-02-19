
import java.io.*;
import java.util.StringTokenizer;

public class Solution {

    public static void add(int v) {
        que[++cnt] = v;
        int cur = cnt;
        while (cur > 1) {
            int parent = cur / 2;
            if (que[parent] < que[cur]) {
                int tmp = que[cur];
                que[cur] = que[parent];
                que[parent] = tmp;

                cur = parent;
            } else {
                break;
            }
        }
    }
    public static int poll() {
        if (cnt == 0) {
            return -1;
        }

        int max = que[1];
        que[1] = que[cnt];
        que[cnt--] = 0;

        int cur = 1;
        while (cur * 2 + 1 <= cnt) {
            int larger = cur;
            int left = cur * 2;
            int right = cur * 2 + 1;

            if (que[left] > que[larger]) {
                larger = left;
            }

            if (que[right] > que[larger]) {
                larger = right;
            }

            if (larger != cur) {
                int tmp = que[cur];
                que[cur] = que[larger];
                que[larger] = tmp;

                cur = larger;
            } else {
                break;
            }
        }

        return max;
    }
    static int que[], cnt;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int TC = Integer.parseInt(br.readLine());
        for (int tc=1; tc<=TC; tc++) {
            bw.write("#" + tc + " ");
            int N = Integer.parseInt(br.readLine());
            que = new int[N];
            cnt = 0;
            for (int i=0; i<N; i++) {
                StringTokenizer st = new StringTokenizer(br.readLine());
                int op = Integer.parseInt(st.nextToken());
                if (op == 1) {
                    add(Integer.parseInt(st.nextToken()));
                } else if (op == 2) {
                    bw.write(poll() + " ");
                }
            }
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
}

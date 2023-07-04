
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static int n, maxValue, day;

    static class Work implements Comparable<Work> {
        int d, w;

        public Work(int d, int w) {
            super();
            this.d = d;
            this.w = w;
        }

        @Override
        public int compareTo(Work o) {
            if (this.d == o.d) return o.w - this.w;
            return o.d - this.d;
        }
    }

    static PriorityQueue<Integer> queue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        Work[] input = new Work[n];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());

            input[i] = new Work(d, w);

            day = day > d ? day : d;
        }
        Arrays.sort(input);

        Work tmp = null;
        Queue<Work> q = new LinkedList<>();
        queue = new PriorityQueue<>();
        int max = 0;
        int idx = 0;
        while (day > 0) {

            while (idx < n && input[idx].d >= day) {
                queue.offer(-input[idx].w);
                idx++;
            }
            day--;
            if (!queue.isEmpty()) {
                maxValue -= queue.poll();
            }

//            Work cur;// = queue.poll();
//            q.offer(cur);
//            if (cur.d >= day) {
//                if (max <= cur.w) {
//                    maxValue -= max;
//                    max = cur.w;
//                    tmp = cur;
//                    maxValue += max;
//                }
//            } else {
//                max = 0;
//                day--;
//                q.remove(tmp);
//                int idx = q.size();
//                for (int i = 0; i < idx; i++) {
//                    queue.offer(q.poll());
//                }
//                continue;
//            }
        }
        System.out.println(maxValue);
    }
}
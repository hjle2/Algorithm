import java.io.*;
import java.lang.reflect.Array;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());


        int[][] stuff = new int[n][2]; // 물건의 정보를 담을 배열
        for (int i=0; i<n; i++) {
            st = new StringTokenizer(br.readLine());
            stuff[i][0] = Integer.parseInt(st.nextToken());// 보석의 무게
            stuff[i][1] = Integer.parseInt(st.nextToken());// 보석의 가격
        }

        int[] bag = new int[k]; // 가방의 정보를 담을 배열
        for (int i=0; i<k; i++) {
            bag[i] = Integer.parseInt(br.readLine());
        }
        // << input

        Arrays.sort(stuff, (a, b)-> {
            if (a[0] == b[0]) {
                return a[1] - b[1]; // 보석의 가격 오름차순 -> 상관 없음
            }
            return a[0] - b[0]; // 보석의 무게 오름차순
        });
        Arrays.sort(bag); // 가방의 무게 오름차순

        PriorityQueue<Integer> steal = new PriorityQueue<>((a, b)-> {
            return b - a;
        });
        long ans = 0;
        int j = 0;
        for (int i=0; i<k; i++) {

            while (j < n && bag[i] >= stuff[j][0]) {
                steal.add(stuff[j][1]);
                j++;
            }

            if (!steal.isEmpty()) {
                ans += steal.poll();
            }
        }

        bw.write("" + ans);
        bw.flush();
        bw.close();
    }
}
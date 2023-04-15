import java.io.*;
import java.sql.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int m = Integer.parseInt(br.readLine());

        int box[][] = new int[m][3];
        for (int i=0; i<m; i++) {
            st = new StringTokenizer(br.readLine());
            box[i][0] = Integer.parseInt(st.nextToken());
            box[i][1] = Integer.parseInt(st.nextToken());
            box[i][2] = Integer.parseInt(st.nextToken());
        }
        // 보내는 마을 번호, 받는 마을 번호, 박스 개수

        Arrays.sort(box, (a, b) -> {
            if (a[1] == b[1])
                return a[0] - b[0];
            return a[1] - b[1];
        });
        // 받는 마을 번호 순으로 정렬

        int ans = 0;
        int truck[] = new int[n];
        for (int i=0; i<n; i++) {
            truck[i] = c; // i위치에서 트럭에 실을 수 있는 박스의 수
        }

        for (int i=0; i<m; i++) {
            int frm = box[i][0];
            int to = box[i][1];
            int boxN = box[i][2];

            int minN = boxN;
            for (int j=frm; j<to; j++) {
                // 실을 수 있는 박스의 개수 구하기
                minN = Math.min(minN, truck[j]);
            }

            for (int j=frm; j<to; j++) {
                truck[j] -= minN;
            }
            ans += minN;
        }
        bw.write("" + ans);
        bw.flush();
        bw.close();
    }
}
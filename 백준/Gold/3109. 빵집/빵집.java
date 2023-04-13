import java.io.*;
import java.util.StringTokenizer;

public class Main {
    static int dx[] = {0, 1, -1};
    static char ar[][];
    static int r, c;
    public static boolean connect_pipe(int x, int y) {
        ar[x][y] = '-';

        if (y == c - 1)
            return true;

        if (x-1 >= 0 && ar[x-1][y+1] == '.' && connect_pipe(x-1, y+1))
            return true;

        if (ar[x][y+1] == '.' && connect_pipe(x, y+1))
            return true;

        if (x+1 < r &&  ar[x+1][y+1] == '.' && connect_pipe(x+1, y+1))
            return true;

        return false;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());

        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        ar = new char[r][c];

        for (int i=0; i<r; i++) {
            st = new StringTokenizer(br.readLine());
            ar[i] = st.nextToken().toCharArray();
        }
        // << input
        int ans = 0;
        for (int i=0; i<r; i++) {
            // 시작점 i, 0
            if (connect_pipe(i, 0))
                ans += 1;
            // 도착지 x, n-1
        }
        bw.write(""+ans);
        bw.flush();
        bw.close();
        br.close();
    }
}
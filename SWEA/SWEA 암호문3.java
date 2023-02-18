import java.io.*;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
    static List<Integer> list;
    static StringTokenizer st;
    public static String solve(int N, int M) {
        // 마지막 N 개의 비트를 확인할 변수
        int bit = (1 << N) - 1;
        int result = bit & M;

        if (result == bit) {
            return "ON";
        }
        return "OFF";
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int TC = 10;

        for (int tc = 1; tc <= TC; tc++) {
            list = new LinkedList<>(); // 암호문을 담을 리스트

            int N = Integer.parseInt(br.readLine()); // 원본 암호문의 길이

            st = new StringTokenizer(br.readLine()); // 원본 암호문
            for (int i=0; i<N; i++) {
                list.add(Integer.parseInt(st.nextToken())); // 리스트에 추가해주기
            }

            int Q = Integer.parseInt(br.readLine()); // 쿼리의 개수
            st = new StringTokenizer(br.readLine()); // 원본 암호문
            for (int i=0; i<Q; i++) {
                char command = st.nextToken().charAt(0);
                int x = Integer.parseInt(st.nextToken());
                func(command, x);
            }
            bw.write(print(tc));
        }
        bw.flush();
        bw.close();
    }
    public static void func(char command, int x) {
        int y;
        switch (command) {
            case 'I':
                y = Integer.parseInt(st.nextToken());
                for (int i=0; i<y; i++) {
                    list.add(x + i, Integer.parseInt(st.nextToken()));
                }
                break;
            case 'D':
                y = Integer.parseInt(st.nextToken());
                for (int i=0; i<y; i++) {
                    list.remove(x);
                }
                break;
            case 'A':
                for (int i=0; i<x; i++) {
                    list.add(Integer.parseInt(st.nextToken()));
                }
                break;
        }
    }

    public static String print(int tc) {
        StringBuilder sb = new StringBuilder();
        sb.append("#");
        sb.append(tc);
        for (int i=0; i < 10; i++) {
            sb.append(" " + list.get(i));
        }
        sb.append("\n");
        return sb.toString();
    }
}

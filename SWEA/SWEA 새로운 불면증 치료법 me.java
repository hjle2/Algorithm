import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Solution {
    public static int solve(int N) {
        int total = (1 << 10) - 1;  // 전체 숫자가 등장했을 떄 visited의 값 0~9bit가 모두 1
        int visited = 0;    // 모든 숫자의 방문 여부 화인할 변수

        for (int cnt = 1; ;cnt++) {
            char[] nArr = String.valueOf(N*cnt).toCharArray();
            for (char c : nArr) {
                int n = c - '0';
                visited |= (1 << n); // 해당 숫자 방문 처리
            }
            if (visited == total) { // 모든 숫자가 등장했다면,
                return cnt * N; // 결과 반환
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int TC = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= TC; tc++) {
            int N = Integer.parseInt(br.readLine());
            System.out.printf("#%d %d", tc, solve(N));
        }
    }
}

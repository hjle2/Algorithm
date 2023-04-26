import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();

        for (int tc = 1; tc <= TC; tc++) {
            long N = sc.nextLong();

            long l = 1;
            long r = 10000000000l;
            long ans = 0;
            while (l <= r) {
                long mid = (l + r) / 2;
                long value = mid * (mid + 1) / 2;

                if (N >= value) {
                    ans = mid;
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            }
            long tmp = ans * (ans + 1) / 2;
            if (N != tmp)
                ans = -1;
            System.out.printf("#%d %d\n", tc, ans);
        }
    }
}
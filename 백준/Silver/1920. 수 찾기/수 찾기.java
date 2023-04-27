import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] an = new int[n];
        for (int i=0; i<n; i++) {
            an[i] = sc.nextInt();
        }
        Arrays.sort(an);

        int m = sc.nextInt();

        int[] am = new int[m];
        for (int i=0; i<m; i++) {
            am[i] = sc.nextInt();
        }

        // << input

        for (int i=0; i<m; i++) {
            System.out.println(solve(n, an, am[i]));
        }
    }

    public static int solve(int n, int[] ar, int m) {
        int l = 0;
        int r = n-1;

        while (l <= r) {
            int mid = (l + r) / 2;

            int value = ar[mid];

            if (value < m) {
                l = mid + 1;
            } else if (value > m) {
                r = mid - 1;
            } else {
                return 1;
            }
        }

        return 0;
    }
}
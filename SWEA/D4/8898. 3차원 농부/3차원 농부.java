import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        int TC = sc.nextInt();
        for (int tc=1; tc<=TC; tc++) {

            int n = sc.nextInt();
            int m = sc.nextInt();

            int dx = Math.abs(sc.nextInt() - sc.nextInt());

            int[] cow = new int[n];
            for (int i=0; i<n; i++) {
                cow[i] = sc.nextInt();
            }
            Arrays.sort(cow);

            int cnt = 0;
            int min = Integer.MAX_VALUE;
            for (int i=0; i<m; i++) {
                int hpos = sc.nextInt();
                int cIdx = binSearch(cow, hpos);


                if (cIdx < cow.length) {
                    int cpos = cow[cIdx];
                    int dz = Math.abs(hpos - cpos);
                    if (min > dz) {
                        min = dz;
                        cnt = 1;
                    } else if (min == dz) {
                        cnt++;
                    }
                }

                if (cIdx > 0) {
                    int cpos = cow[cIdx-1];
                    int dz = Math.abs(hpos - cpos);
                    if (min > dz) {
                        min = dz;
                        cnt = 1;
                    } else if (min == dz) {
                        cnt++;
                    }
                }
            }

            System.out.printf("#%d %d %d\n", tc, Math.abs(dx + min), cnt);
        }
    }

    public static int binSearch(int[] ar, int value) {

        int l = 0;
        int r = ar.length-1;

        if (ar[l] > value) {
            return l;
        } else if (ar[r] < value) {
            return r;
        }

        int mid = ar.length;

        while (l <= r) {
            mid = (l + r) / 2;

            if (ar[mid] == value) {
                return mid;
            } else if (ar[mid] > value) {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        // 같거나 큰 소 중에서 가장 왼쪽의 인덱스를 반환한다
        if (ar[mid] < value) {
            mid ++;
        }
        return mid;
    }
}
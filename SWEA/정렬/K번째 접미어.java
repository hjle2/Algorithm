import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Solution {
    public static String solve(int k, String word) {
        int th = 0;
        int length = word.length();

        if (length < k)
            return "none";
        List<String> tail = new ArrayList<>();
        for (int i=0; i<length; i++) {
            tail.add(word.substring(i));
        }
        Collections.sort(tail);
        return tail.get(k-1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for (int tc=1; tc<=TC; tc++) {
            int k = sc.nextInt();
            System.out.printf("#%d %s\n", tc, solve(k, sc.next()));
        }
    }
}

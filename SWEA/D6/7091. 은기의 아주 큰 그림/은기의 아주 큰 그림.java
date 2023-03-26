import java.util.Scanner;

public class Solution {
    // int의 MAX
    final static int HASH_SIZE = (int)Math.pow(2, 30) - 1;
    final static int horizonHash = 4; // 해시 함수에서 사용할 숫자
    final static int verticalHash = 5; // 해시 함수에서 사용할 숫자

    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int TC = sc.nextInt();
        for (int tc = 1; tc <= TC; tc++) {
            int H = sc.nextInt();
            int W = sc.nextInt();
            int N = sc.nextInt();
            int M = sc.nextInt();

            int[][] dream = new int[H][W];
            int[][] draw = new int[N][M];

            for (int i=0; i<H; i++) {
                String str = sc.next();
                for (int j=0; j<W; j++) {
                    dream[i][j] = str.charAt(j) == 'o' ? 1 : 0;
                }
            }

            for (int i=0; i<N; i++) {
                String str = sc.next();
                for (int j=0; j<M; j++) {
                    draw[i][j] = str.charAt(j) == 'o' ? 1 : 0;
                }
            }
            System.out.printf("#%d %d\n", tc, solution(dream, draw));
        }

    }

    static int solution(int[][] draw, int[][] dream) {
        // 선생님이 그린 그림
        int H = draw.length;
        int W = draw[0].length;
        // 은주가 꿈에서 본 그림
        int N = dream.length;
        int M = dream[0].length;
        int hashVal = getHash(draw, H, W)[0][0];
        int[][] hashArr = getHash(dream, H, W);
        int cnt = 0;
        for (int i=0; i<=N-H; i++) {
            for (int j=0; j<=M-W; j++) {
                cnt = hashArr[i][j] == hashVal ? cnt + 1 : cnt;
            }
        }
        return cnt;
    }

    /**
     *
     * @param matrix: hash값을 구할 2차 배열
     * @param height: 구할 해시의 높이 단위
     * @param width: 구할 해시의 넓이 단위
     * @return 구한 해시의 배열 값
     */
    static int[][] getHash(int[][] matrix, int height, int width) {
        int H = matrix.length;
        int W = matrix[0].length;

        // 1. 먼저 가로 해시값을 구한다.
        int[][] horizonHashArr = new int[H][W - width + 1];
        int horizonMaxP = getMaxPower(width, horizonHash); // 가장 앞자리를 제거하기 위한 MaxPower숫자를 구한다

        for (int i=0; i<H; i++) {
            int hash = getHorizonHash(matrix, width, i, 0);
            horizonHashArr[i][0] = hash;
            for (int j=1; j<=W-width; j++) {
                horizonHashArr[i][j] = getNext(horizonHashArr[i][j-1], matrix[i][j-1], horizonMaxP, matrix[i][j-1+width], horizonHash);
            }
        }

        // 2. 가로 해시 값에서 세로 해시값을 구한다
        int verticalMaxP = getMaxPower(height, verticalHash);
        int[][] verticalHashArr = new int[H - height + 1][W - width + 1];
        for (int j=0; j<=W-width; j++) {
            int hash = getVerticalHash(horizonHashArr, height, 0, j);
            verticalHashArr[0][j] = hash;
            for (int i=1; i<=H-height; i++) {
                verticalHashArr[i][j] = getNext(verticalHashArr[i-1][j], horizonHashArr[i-1][j], verticalMaxP, horizonHashArr[i-1+height][j], verticalHash);
            }
        }
        return verticalHashArr;
    }

    static int getMaxPower(int len, int shift) {
        int result = 1;
        for (int i=0; i < len - 1; i++) { // len - 1 인 이유? 첫번째 자리는 0 or 1
            result = (result << shift) + result;
        }
        return result; // 해시 테이블의 사이즈 HASH_SIZE 해시 테이블의 주소값 반환하기
    }

    static int getHorizonHash(int[][] matrix, int len, int row, int col) {
        int result = 0;
        for (int i=0; i<len; i++) {
            // result << 4 는 result * 16과 동일
            // (result << 4) + result 는 result * 17과 동일
            // 소수 17을 사용
            result = (result << horizonHash) + result + matrix[row][col + i];
        }
        return result;
    }

    static int getVerticalHash(int[][] matrix, int len, int row, int col) {
        int result = 0;
        for (int i=0; i<len; i++) {
            // result << 5 는 result * 32과 동일
            // (result << 5) + result 는 result * 33과 동일
            // 소수 33을 사용
            result = (result << verticalHash) + result + matrix[row + i][col];
        }
        return result;
    }

    static int getNext(int prev, int del, int maxPower, int add, int shift) {
        int result = prev - del * maxPower; // 맨 앞자리의 숫자 제거
        result = (result << shift) + result + add; // 현재 해쉬를 1bit 밀고, 한자리 추가
        return result;
    }
}
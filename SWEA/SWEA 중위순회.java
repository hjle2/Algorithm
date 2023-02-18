import java.io.*;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
    static char[] tree;
    static char[] word;
    static int index;
    public static void inorder(int N, int cur) {
        if (cur * 2 <= N) { // 왼쪽 자식노드가 있다면, 
            inorder(N, cur * 2); // 왼쪽 자식노드를 탐색
        }
        word[index++] = tree[cur]; // 현재 노드를 탐색

        if (cur * 2 + 1 <= N) { // 오른쪽 자식노드가 있다면, 
            inorder(N, cur * 2 + 1); // 오르쪽 자식노드를 탐색
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int TC = 10;

        for (int tc = 1; tc <= TC; tc++) {
            int N = Integer.parseInt(br.readLine()); // 정점의 총 수
            index = 0;
            tree = new char[N+1];  // 트리 그래프 값을 저장할 배열
            word = new char[N]; // 트리를 inorder로 읽었을 떄의 단어를 저장할 배열

            for (int i=0; i<N; i++) { // 정점의 개수만큼 tree 구성하기

                StringTokenizer st = new StringTokenizer(br.readLine());

                int n = Integer.parseInt(st.nextToken()); // 정점 번호

                char c = st.nextToken().charAt(0); // 정점의 문자
                tree[n] = c;
            }
            inorder(N, 1); // tree의 top부터 inorder탐색 시작
            bw.write("#" + tc + " " + String.valueOf(word) + "\n");
        }
        bw.flush();
        bw.close();
    }
}

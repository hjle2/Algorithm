import java.io.*;
import java.util.StringTokenizer;

public class Solution { // _2_공통조상
    public static int getChildCnt(Node node) {
        int cnt = 1; // 현재 노드 1개

        if (node.left != null) {
            cnt += getChildCnt(node.left); // 왼쪽 자식노드를 루트로하는 서브트리의 크기
        }
        if (node.right != null) {
            cnt += getChildCnt(node.right); // 오른쪽 자식노드를 루트로하는 서브트리의 크기
        }
        return cnt;
    }

    public static int getCommonParentNode(Node n1, Node n2) {
        boolean[] visited = new boolean[V + 1];
        while (n1.parent != null) { // 가장 위의 부모노드라면 탐색 중지
            visited[n1.data] = true; // 방문 체크
            n1 = n1.parent; // 현재 노드의 부모 노드 탐색
        }

        while (n2.parent != null) {
            if (visited[n2.data]) { // 가장 가까운 공통 부모노드
                return n2.data; // 공통의 부모를 찾으면 바로 반환시켜서 가까운 값을 구할 수 있도록 한다.
            }
            n2 = n2.parent; // 현재 노드의 부모 노드 탐색
        }
        return 0;
    }
    static class Node {
        int data;
        Node left;  // 왼쪽 자식노드
        Node right; // 오른쪽 자식노드
        Node parent; // 부모 노드
    }
    static int V;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int TC = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= TC; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            // 정점의 개수, 간선의 개수, 공통 조상을 찾는 두 정점의 번호
            int E, n1, n2;
            V = Integer.parseInt(st.nextToken());
            E = Integer.parseInt(st.nextToken());
            n1 = Integer.parseInt(st.nextToken());
            n2 = Integer.parseInt(st.nextToken());

            Node[] tree = new Node[V+1];
            for (int i=1; i<=V; i++) {
                tree[i] = new Node();
                tree[i].data = i; // i번 노드의 번호는 i
            }
            tree[1].data = 1; // 루트 노드의 노드번호는 1


            st = new StringTokenizer(br.readLine());
            // 간선 (부모-자식)
            for (int i=0; i<E; i++) {
                int p = Integer.parseInt(st.nextToken()); // 부모 노드 번호
                int c = Integer.parseInt(st.nextToken()); // 자식 노드 번호

                if (tree[p].left == null) { // 왼쪽 노드에 먼저 연걸
                    tree[p].left = tree[c];
                } else {                    // 이미 왼쪽 노드에 연결 됐으면 오른쪽 노드에 연결
                    tree[p].right = tree[c];
                }
                tree[c].parent = tree[p];
            }
            int commonParent = getCommonParentNode(tree[n1], tree[n2]);
            bw.write("#" + tc + " " + commonParent + " " + getChildCnt(tree[commonParent]));
            bw.write("\n");
        }
        bw.flush();
        bw.close();
    }
}

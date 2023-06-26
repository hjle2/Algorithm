import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    static int n, max;

    static class Route {
        int[][] map;
        int cnt;

        public Route(int[][] map, int cnt) {
            this.map = map;
            this.cnt = cnt;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int[][] map = new int[n][n];
        max = 0;
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        bfs(map);

        System.out.println(max);
    }

    private static void bfs(int[][] m_map) {
        Queue<Route> queue = new LinkedList<>();
        queue.add(new Route(m_map, 5));

        while (!queue.isEmpty()) {
            Route nr = queue.poll();
            int map[][] = nr.map;
            int depth = nr.cnt;
            if (depth == 0) {
                for (int r = 0; r < n; r++) {
                    for (int c = 0; c < n; c++) {
                        max = Math.max(max, map[r][c]);
                    }
                }
                continue;
            }
            for (int i = 0; i < 4; i++) {
                int[][] new_map = new int[n][n];
                Stack<Integer> stack = new Stack<>();
                if (i == 0) {//상
                    for (int c = 0; c < n; c++) {
                        boolean flag = false;
                        for (int r = 0; r < n; r++) {
                            if (map[r][c] != 0)
                                stack.push(map[r][c]);
                            else continue;
                            if (stack.size() < 2) continue;

                            int first = stack.pop();
                            int second = stack.pop();
                            if (first == second && !flag) {
                                stack.push(first * 2);
                                flag = true;
                            } else {
                                stack.push(second);
                                stack.push(first);
                                flag = false;
                            }
                        }
                        for (int j = stack.size(); j < n; j++) {
                            stack.push(0);
                        }
                        for (int j = n - 1; j >= 0; j--) {
                            new_map[j][c] = stack.pop();
                        }
                    }
                } else if (i == 1) {//하
                    for (int c = 0; c < n; c++) {
                        boolean flag = false;
                        for (int r = n - 1; r >= 0; r--) {
                            if (map[r][c] != 0)
                                stack.push(map[r][c]);
                            else continue;
                            if (stack.size() < 2) continue;

                            int first = stack.pop();
                            int second = stack.pop();
                            if (first == second && !flag) {
                                stack.push(first * 2);
                                flag = true;
                            } else {
                                stack.push(second);
                                stack.push(first);
                                flag = false;
                            }
                        }
                        for (int j = stack.size(); j < n; j++) {
                            stack.push(0);
                        }
                        for (int j = 0; j < n; j++) {
                            new_map[j][c] = stack.pop();
                        }
                    }
                } else if (i == 2) {//좌
                    for (int r = 0; r < n; r++) {
                        boolean flag = false;
                        for (int c = 0; c < n; c++) {
                            if (map[r][c] != 0)
                                stack.push(map[r][c]);
                            else continue;
                            if (stack.size() < 2) continue;

                            int first = stack.pop();
                            int second = stack.pop();
                            if (first == second && !flag) {
                                stack.push(first * 2);
                                flag = true;
                            } else {
                                stack.push(second);
                                stack.push(first);
                                flag = false;
                            }
                        }
                        for (int j = stack.size(); j < n; j++) {
                            stack.push(0);
                        }
                        for (int j = n - 1; j >= 0; j--) {
                            new_map[r][j] = stack.pop();
                        }
                    }
                } else if (i == 3) {//우
                    for (int r = 0; r < n; r++) {
                        boolean flag = false;
                        for (int c = n - 1; c >= 0; c--) {
                            if (map[r][c] != 0)
                                stack.push(map[r][c]);
                            else continue;
                            if (stack.size() < 2) continue;

                            int first = stack.pop();
                            int second = stack.pop();
                            if (first == second && !flag) {
                                stack.push(first * 2);
                                flag = true;
                            } else {
                                stack.push(second);
                                stack.push(first);
                                flag = false;
                            }
                        }
                        for (int j = stack.size(); j < n; j++) {
                            stack.push(0);
                        }
                        for (int j = 0; j < n; j++) {
                            new_map[r][j] = stack.pop();
                        }
                    }
                }
//한번 돌리고 나서 최댓값 찾기
                queue.offer(new Route(new_map, depth - 1));
            }
        }

    }
}

//반례
//3
//0 8 1024
//4 0 4
//0 1024 32
//output: 1024
//correct answer: 2048
//6
//2 0 0 0 0 0
//2 0 0 0 0 0
//2 0 0 0 0 0
//4 0 0 0 0 0
//8 0 0 0 0 0
//8 0 0 0 0 0

//7
//2 2 2 2 2 2 2
//2 0 2 2 2 2 2
//2 0 2 2 2 2 2
//2 0 2 2 2 2 2
//2 2 2 0 2 2 2
//2 2 2 2 2 2 0
//2 2 2 2 2 2 0
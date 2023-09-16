import java.util.Stack;
import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        Stack<Integer> s = new Stack<>();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int N = Integer.parseInt(br.readLine());
        
        for (int i=0; i<N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String cmd = st.nextToken();
            switch (cmd) {
                case "push":
                    s.push(Integer.parseInt(st.nextToken()));
                break;
                case "pop":
                    bw.write(s.pop() + "\n");
                break;
                case "size":
                    bw.write(s.size() + "\n");
                break;
                case "empty":
                int j = 0;
                if (s.empty()) {
                    j = 1;
                }
                    bw.write(j + "\n");
                break;
                case "top":
                    bw.write(s.peek() + "\n");
                break;
            }
        }
        bw.flush();
        bw.close();
    }
}

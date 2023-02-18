import java.io.*;
import java.util.*;

public class Main {
    static class Node {
        // Node prev;
        int data;
        Node nxt;
        Node prv;

        public Node(int data) {
            this.data = data;
        }
    }
    static class DLL {
        int nodeCnt;
        Node head;
        Node tail;

        public void push_front(int t) {
            Node newNode = new Node(t);
            if (nodeCnt > 0) { // DDL에 자료가 있을 때
                if (head == null) { // tail에 자료가 있을 때
                    head = newNode;
                    head.nxt = tail;
                    tail.prv = head;
                }
                else {
                    if (tail == null) { // head에만 자료가 있을 때
                        head.prv = newNode;
                        newNode.nxt = head;
                        tail = head;
                        head = newNode;
                    } else {        // head, tail모두 자료가 있을 때
                        head.prv = newNode;
                        newNode.nxt = head;
                        head = newNode;
                    }
                }
            }
            else {
                head = newNode; // 헤드에 데이터 추가
            }
            ++nodeCnt;
        }
        public void push_back(int t) {
            Node newNode = new Node(t);
            if (nodeCnt > 0) {
                if (tail == null) {
                    tail = newNode;
                    tail.prv = head;
                    head.nxt = tail;
                } else {
                    if (head == null) {
                        head = tail;
                        tail = newNode;
                        head.nxt = tail;
                        tail.prv = head;
                    } else {
                        tail.nxt = newNode;
                        newNode.prv = tail;
                        tail = newNode;
                    }
                }
            } else {
                tail = newNode;
            }
            ++nodeCnt;
        }
        public int pop_front() {
            int front;
            if (head == null) {
                front = tail.data;
                tail = null;
            } else if (tail == null) {
                front = head.data;
                head = null;
            } else {
                front = head.data;
                if (nodeCnt > 2) {
                    head = head.nxt;
                    head.prv = null;
                } else {
                    head = null;
                }
            }
            --nodeCnt;
            return front;
        }
        public int pop_back() {
            int back;
            if (head == null) {
                back = tail.data;
                tail = null;
            } else if (tail == null) {
                back = head.data;
                head = null;
            } else {
                back = tail.data;
                if (nodeCnt > 2) {
                    tail = tail.prv;
                    tail.nxt = null;
                } else {
                    tail = null;
                }
            }
            --nodeCnt;
            return back;
        }
        public int size() {
            return nodeCnt;
        }
        public int empty() {
            if (nodeCnt == 0) {
                return 1;
            } else {
                return 0;
            }
        }
        public int front() {
            if (head == null) {
                return tail.data;
            }
            return head.data;
        }
        public int back() {
            if (tail == null) {
                return head.data;
            }
            return tail.data;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        DLL dll = new DLL();
        int Q = Integer.parseInt(br.readLine());

        for (int i=0; i<Q; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            int x;
            switch(command) {
                case "push_back":
                    x = Integer.parseInt(st.nextToken());
                    dll.push_back(x);
                break;
                case "push_front":
                    x = Integer.parseInt(st.nextToken());
                    dll.push_front(x);
                break;
                case "pop_front":
                    System.out.println(dll.pop_front());
                break;
                case "pop_back":
                    System.out.println(dll.pop_back());
                break;
                case "size":
                    System.out.println(dll.size());
                break;
                case "empty":
                    System.out.println(dll.empty());
                break;
                case "front": // peek
                    System.out.println(dll.front());
                break;
                case "back":
                    System.out.println(dll.back());
                break;
            }
        }
    }
}


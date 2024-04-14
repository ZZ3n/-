import java.io.*;
import java.util.*;

/*
 * 1. 조건 : NxN 크기의 땅, 각 칸은 (r,c) -> 1부터 시작, 처음 모든 칸엔 양분 5씩, M개 나무 (같은 칸에 여러 개 심을 수 있음)
 * 2. 과정
 *  1) 봄
 *      -> 나무가 나이만큼 양분을 먹고 나이 1 증가 (같은 칸에 있는 양분만 먹을 수 있음)
 *      -> 하나의 칸에 여러 나무가 있다면 나이가 어린 나무부터 양분을 먹음
 *      -> 만약 양분이 부족해 나이만큼 양분을 먹을 수 없는 나무는 즉시 죽음
 *  2) 여름
 *      -> 봄에 죽은 나무가 양분으로 변함. 각 죽은 나무마다 나이를 2로 나눈 값이 같은 칸 양분으로 추가 (소수점 버림)
 *  3) 가을
 *      -> 나무가 번식. 번식하는 나무의 나이는 5의 배수여야 함
 *      -> 인접한 8개의 칸에 나이가 1인 나무가 생김 (땅을 벗어난 곳은 제외)
 *  4) 겨울
 *      -> 땅을 돌아다니면서 땅에 양분을 추가. 각 칸에 추가되는 양분은 A[r][c]
 * 3. 정답 : K년이 지난 후 살아있는 나무의 개수
 */

public class Jun2 {
    static class Tree implements Comparable {
        int row, col;
        int age;
        boolean isDead;

        public Tree(int row, int col, int age) {
            this.row = row;
            this.col = col;
            this.age = age;
            this.isDead = false;
        }

        @Override
        public int compareTo(Object o) {
            Tree tree = (Tree) o;
            return this.age - tree.age;
        }
    }

    static int N, M, K;
    static int[][] food;    // 추가 양분 정보
    static int[][] ground;  // 땅별 양분 정보
    static PriorityQueue<Tree> trees;
    static Queue<Tree> deadTrees;


    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(bf.readLine());

        N = Integer.parseInt(stk.nextToken());
        M = Integer.parseInt(stk.nextToken());
        K = Integer.parseInt(stk.nextToken());

        food = new int[N + 1][N + 1];
        ground = new int[N + 1][N + 1];
        trees = new PriorityQueue<>();
        deadTrees = new ArrayDeque<>();

        // 양분 정보 저장
        for (int i = 1; i <= N; i++) {
            stk = new StringTokenizer(bf.readLine());
            for (int j = 1; j <= N; j++) {
                food[i][j] = Integer.parseInt(stk.nextToken());
                ground[i][j] = 5;
            }
        }

        // 나무 정보 저장
        for (int i = 0; i < M; i++) {
            stk = new StringTokenizer(bf.readLine());
            int row = Integer.parseInt(stk.nextToken());
            int col = Integer.parseInt(stk.nextToken());
            int age = Integer.parseInt(stk.nextToken());
            trees.offer(new Tree(row, col, age));
        }

        // K년 동안 재테크
        for (int i = 1; i <= K; i++) {
            simulation();
        }

        System.out.print(trees.size());
    }

    private static void simulation() {
        spring();
        summer();
        autumn();
        winter();
    }

    private static void spring() {
        for (Tree tree : trees) {
            if (ground[tree.row][tree.col] < tree.age) {    // 양분이 나이보다 적은 경우
                tree.isDead = true;
                deadTrees.offer(tree);
                continue;
            }
            ground[tree.row][tree.col] -= tree.age; // 어린 나무부터 나이만큼 양분을 먹음
            tree.age += 1; // 나이 1 증가
        }
    }

    private static void summer() {
        while (!deadTrees.isEmpty()) {
            Tree deadTree = deadTrees.poll();
            ground[deadTree.row][deadTree.col] += deadTree.age / 2; // 양분 추가
        }
    }

    private static void autumn() {
        int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
        int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};
        PriorityQueue<Tree> newTrees = new PriorityQueue<>();

        for (Tree tree : trees) {
            if (tree.isDead) {
                continue;
            }
            if (tree.age % 5 == 0) {
                int row = tree.row;
                int col = tree.col;
                for (int i = 0; i < 8; i++) {
                    int nextRow = row + dx[i];
                    int nextCol = col + dy[i];
                    if (nextRow >= 1 && nextRow <= N && nextCol >= 1 && nextCol <= N) {
                        newTrees.offer(new Tree(nextRow, nextCol, 1));    // 만약 trees 에 추가한다면 ConcurrentModificationException 발생
                    }
                }
            }
        }
        for (Tree tree : trees) {
            if (!tree.isDead) {
                newTrees.offer(tree);
            }
        }
        trees = newTrees;
    }

    private static void winter() {
        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                ground[i][j] += food[i][j];
            }
        }
    }
}

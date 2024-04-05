import java.io.*;
import java.util.*;

public class jun2 {
    static int MAX = Integer.MIN_VALUE;
    static int MIN = Integer.MAX_VALUE;

    static int N;
    static int[] numbers;
    static int[] operations;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(bf.readLine());
        numbers = new int[N];
        operations = new int[4];

        StringTokenizer stk = new StringTokenizer(bf.readLine());
        for (int i = 0; i < N; i++) {
            numbers[i] = Integer.parseInt(stk.nextToken());
        }

        stk = new StringTokenizer(bf.readLine());
        for (int i = 0; i < 4; i++) {
            operations[i] = Integer.parseInt(stk.nextToken());
        }

        dfs(1, numbers[0]);

        System.out.println(MAX);
        System.out.println(MIN);
    }

    private static void dfs(int depth, int total) {
        if (depth == N) {
            MAX = Math.max(MAX, total);
            MIN = Math.min(MIN, total);
            return;
        }

        for (int i = 0; i < 4; i++) {
            if (operations[i] > 0) {
                operations[i]--;
                if (i == 0) {
                    dfs(depth + 1, total + numbers[depth]);
                } else if (i == 1) {
                    dfs(depth + 1, total - numbers[depth]);
                } else if (i == 2) {
                    dfs(depth + 1, total * numbers[depth]);
                } else {
                    dfs(depth + 1, total / numbers[depth]);
                }
                operations[i]++;
            }
        }
    }
}

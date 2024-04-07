import java.io.*;
import java.util.*;

/*
 * 문제 : 백준 14501 퇴사 - 실버3
 * 목표 : N+1일째 되는 날 퇴사, N일 동안 상담으로 얻을 수 있는 최대 수익 구하기
 * 주의사항 : 상담 기간엔 다른 상담 불가, N+1일째에는 상담 불가
 */

public class jun2 {
    static int MAX = Integer.MIN_VALUE;
    static int N;
    static int[] day;
    static int[] cost;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(bf.readLine());
        day = new int[N];
        cost = new int[N];

        for (int i = 0; i < N; i++) {
            StringTokenizer stk = new StringTokenizer(bf.readLine());
            day[i] = Integer.parseInt(stk.nextToken());
            cost[i] = Integer.parseInt(stk.nextToken());
        }

        dfs(0, 0);
        System.out.println(MAX);
    }

    private static void dfs(int depth, int totalCost) {
        if (depth >= N) {
            MAX = Math.max(MAX, totalCost);
            return;
        }

        if (depth + day[depth] <= N) {
            dfs(depth + day[depth], totalCost + cost[depth]);   // 상담 가능한 경우
        } else {
            dfs(depth + day[depth], totalCost); // 상담 불가능한 경우
        }
        dfs(depth + 1, totalCost);  // 모든 날짜
    }
}

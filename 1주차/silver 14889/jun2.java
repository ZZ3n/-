import java.io.*;
import java.util.*;

/*
 * 1. 팀을 나눌 수 있는 모든 경우를 찾는 로직
 * 2. 팀을 나눴을 때 각 팀의 능력치를 계산하는 로직
 * 3. 각 팀의 능력치 차가 더 작다면 최솟값을 갱신하는 로직
 */

public class jun2 {
    static int N;
    static int[][] S;
    static boolean[] team;
    static int MIN = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());

        S = new int[N + 1][N + 1];
        team = new boolean[N + 1];

        for (int i = 1; i <= N; i++) {
            StringTokenizer stk = new StringTokenizer(bf.readLine());
            for (int j = 1; j <= N; j++) {
                S[i][j] = Integer.parseInt(stk.nextToken());
            }
        }

        makeTeam(1, 0);
        System.out.println(MIN);
    }

    private static void makeTeam(int number, int teamSize) {
        if (teamSize == N / 2) {
            calculateStat();
            return;
        }

        for (int i = number; i <= N; i++) {
            if (!team[i]) {
                team[i] = true;
                makeTeam(i + 1, teamSize + 1);
                team[i] = false;
            }
        }
    }

    private static void calculateStat() {
        int start = 0;  // true
        int link = 0;   // false

        for (int i = 1; i <= N - 1; i++) {
            for (int j = i + 1; j <= N; j++) {
                if (team[i] && team[j]) {
                    start += S[i][j];
                    start += S[j][i];
                } else if (!team[i] && !team[j]){
                    link += S[i][j];
                    link += S[j][i];
                }
            }
        }

        int diff = Math.abs(start - link);

        if (diff == 0) {
            System.out.println(0);
            System.exit(0);
        }

        MIN = Math.min(MIN, diff);
    }
}

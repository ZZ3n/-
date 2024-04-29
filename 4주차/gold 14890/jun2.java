import java.io.*;
import java.util.*;

/*
 * 1) 경사로 놓는 조건
 * - 낮은 칸과 높은 칸의 높이 차는 1이어야 함
 * - 경사로는 낮은 칸에 놓으며, L개의 연속 칸의 경사로 바닥은 모두 바닥에 접해야 함
 * - 경사로를 놓을 낮은 칸의 높이는 모두 같아야 함. + L개 칸이 연속되어야 함
 *
 * 2) 필요 로직
 * - 경사로를 놓아야하는지 판단하는 로직
 * - 경사로를 놓는 로직
 * - 유효한 경사로인지 확인하는 로직
 * - 지나갈 수 있는 길인지 확인하는 로직
 */

public class jun2 {
    static int N;
    static int L;
    static int[][] map;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(bf.readLine());

        // 입력
        N = Integer.parseInt(stk.nextToken());
        L = Integer.parseInt(stk.nextToken());
        map = new int[N][N];

        for (int i = 0; i < N; i++) {
            stk = new StringTokenizer(bf.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(stk.nextToken());
            }
        }

        calculateAnswer();

        System.out.println(answer);
    }

    private static void calculateAnswer() {
        for (int i = 0; i < N; i++) {
            boolean isPossibleWidth = checkRow(i);  // 가로 계산
            boolean isPossibleLength = checkColumn(i);  // 세로 계산

            if (isPossibleWidth) {
                answer++;
            }
            if (isPossibleLength) {
                answer++;
            }
        }
    }

    private static boolean checkRow(int row) {
        boolean[] slope = new boolean[N];   // true: 경사로 설치, false: 경사로 미설치

        for (int i = 0; i < N - 1; i++) {
            int diff = map[row][i] - map[row][i + 1];

            // 높이 차이가 1을 넘는 경우
            if (diff > 1 || diff < -1) {
                return false;
            } else if (diff == 1) {     // 위 -> 아래
                for (int j = 1; j <= L; j++) {
                    if (N <= i + j || slope[i + j]) {
                        return false;
                    }
                    if (map[row][i] - 1 != map[row][i + j]) {
                        return false;
                    }
                    slope[i + j] = true;
                }
            } else if (diff == -1) {    // 아래 -> 위
                for (int j = 0; j < L; j++) {
                    if (i - j < 0 || slope[i - j]) {
                        return false;
                    }
                    if (map[row][i] != map[row][i - j]) {
                        return false;
                    }
                    slope[i - j] = true;
                }
            }
        }
        return true;
    }

    private static boolean checkColumn(int col) {
        boolean[] slope = new boolean[N];   // true: 경사로 설치, false: 경사로 미설치

        for (int i = 0; i < N - 1; i++) {
            int diff = map[i][col] - map[i + 1][col];

            // 높이 차이가 1을 넘는 경우
            if (diff > 1 || diff < -1) {
                return false;
            } else if (diff == 1) {     // 위 -> 아래
                for (int j = 1; j <= L; j++) {
                    if (N <= i + j || slope[i + j]) {
                        return false;
                    }
                    if (map[i][col] - 1 != map[i + j][col]) {
                        return false;
                    }
                    slope[i + j] = true;
                }
            } else if (diff == -1) {    // 아래 -> 위
                for (int j = 0; j < L; j++) {
                    if (i - j < 0 || slope[i - j]) {
                        return false;
                    }
                    if (map[i][col] != map[i - j][col]) {
                        return false;
                    }
                    slope[i - j] = true;
                }
            }
        }
        return true;
    }
}

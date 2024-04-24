import java.io.*;
import java.util.*;

/*
 * 1) NxN 공간에 물고기 M마리 + 아기 상어 1마리, 공간은 1x1 크기의 정사각형 칸, 한 칸에 최대 1마리 물고기
 * 2) 아기 상어와 물고기는 자연수 크기를 가짐. 처음 아기 상어 크기는 2, 1초에 상하좌우 인접한 한 칸씩 이동
 * 3) 아기 상어 조건 : 자신의 크기보다 큰 물고기가 있는 칸 이동x, 자신의 크기보다 작은 물고기만 먹을 수 있음
 * 4) 아기 상어 이동 조건
 *   i) 더 이상 먹을 수 있는 물고기가 없다면 엄마 상어에게 도움 요청
 *   ii) 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 감
 *   iii) 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 감
 *      -> 거리가 가까운 물고기가 많다면, 가장 위 물고기 -> 가장 왼쪽 물고기 순으로 먹음
 * 5) 이동 시간은 1초, 이동과 동시에 물고기를 먹으면 해당 칸은 빈 칸이 됨
 * 6) 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가
 * 7) 아기 상어가 몇 초동안 엄마 상어 도움 없이 물고기를 잡아먹을 수 있는지?
 * 8) 공간 상태
 *      -> 0: 빈 칸 / 1,2,3,4,5,6: 칸에 있는 물고기 크기 / 9: 아기 상어 위치
 */

public class jun2 {
    static class Fish {
        int x, y;
        int time;

        public Fish(int x, int y, int time) {
            this.x = x;
            this.y = y;
            this.time = time;
        }
    }

    static int N;
    static int[][] map;
    static boolean[][] visited;

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    static Fish shark;
    static int sharkSize = 2;
    static int fishCount = 0;
    static List<Fish> canEatFish = new ArrayList<>();
    static int result = 0;

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        map = new int[N][N];
        visited = new boolean[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer stk = new StringTokenizer(bf.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(stk.nextToken());
                if (map[i][j] == 9) {
                    shark = new Fish(i, j, 0);
                    map[i][j] = 0;
                }
            }
        }

        simulation();

        System.out.println(result);
    }

    private static void simulation() {
        Queue<Fish> q = new ArrayDeque<>();
        q.offer(shark);
        visited[shark.x][shark.y] = true;

        while (true) {
            while (!q.isEmpty()) {
                Fish now = q.poll();
                int time = now.time;

                for (int i = 0; i < 4; i++) {
                    int nx = now.x + dx[i];
                    int ny = now.y + dy[i];

                    if (nx < 0 || nx >= N || ny < 0 || ny >= N || visited[nx][ny]) {
                        continue;
                    }

                    // 먹을 수 있는 있는 물고기 -> 먹이 리스트에 추가
                    if (map[nx][ny] < sharkSize && map[nx][ny] != 0) {
                        q.offer(new Fish(nx, ny, time + 1));
                        visited[nx][ny] = true;
                        canEatFish.add(new Fish(nx, ny, time + 1));
                    }

                    // 이동 가능한 경우
                    if (map[nx][ny] == sharkSize || map[nx][ny] == 0) {
                        q.offer(new Fish(nx, ny, time + 1));
                        visited[nx][ny] = true;
                    }
                }
            }

            if (!canEatFish.isEmpty()) {
                eatFish();
                q.clear();
                visited = new boolean[N][N];

                q.offer(shark);
                visited[shark.x][shark.y] = true;
            } else {
                break;
            }
        }
    }

    private static void eatFish() {
        Collections.sort(canEatFish, new Comparator<Fish>() {
            @Override
            public int compare(Fish o1, Fish o2) {
                if (o1.time == o2.time) {
                    if (o1.x == o2.x) {
                        return o1.y - o2.y;
                    }
                    return o1.x - o2.x;
                }
                return o1.time - o2.time;
            }
        });

        Fish now = canEatFish.get(0);

        // 먹이 위치로 상어 이동
        shark.x = now.x;
        shark.y = now.y;

        // 상어 크기 증가
        if (++fishCount == sharkSize) {
            sharkSize++;
            fishCount = 0;
        }

        result += now.time;
        map[now.x][now.y] = 0;

        canEatFish.clear();
    }
}

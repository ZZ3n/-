import java.io.*;
import java.util.*;

public class jun2 {
    static class Seat {
        int x, y;
        int emptyCount;
        int likeCount;

        public Seat(int x, int y, int emptyCount, int likeCount) {
            this.x = x;
            this.y = y;
            this.emptyCount = emptyCount;
            this.likeCount = likeCount;
        }
    }

    static int N;
    static int[][] classRoom;
    static Map<Integer, int[]> map;
    static int result = 0;

    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};


    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(bf.readLine());
        classRoom = new int[N][N];
        map = new HashMap<>();

        for (int i = 0; i < N * N; i++) {
            StringTokenizer stk = new StringTokenizer(bf.readLine());

            int studentNumber = Integer.parseInt(stk.nextToken());
            int[] likeFriends = new int[4];

            for (int j = 0; j < 4; j++) {
                likeFriends[j] = Integer.parseInt(stk.nextToken());
            }

            map.put(studentNumber, likeFriends);

            seatStudent(studentNumber);
        }

        calculateScore();
        System.out.println(result);
    }

    static void seatStudent(int studentNumber) {
        int[] friends = map.get(studentNumber);
        List<Seat> seats = new ArrayList<>();

        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                int emptyCount = 0;
                int likeCount = 0;

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                        continue;
                    }

                    // 좋아하는 친구 확인
                    for (int j = 0; j < 4; j++) {
                        int likeFriend = friends[j];
                        if (classRoom[nx][ny] == likeFriend) {
                            likeCount++;
                        }
                    }

                    // 빈 자리 확인
                    if (classRoom[nx][ny] == 0) {
                        emptyCount++;
                    }
                }
                seats.add(new Seat(x, y, emptyCount, likeCount));
            }
        }

        Collections.sort(seats, new Comparator<Seat>() {
            @Override
            public int compare(Seat o1, Seat o2) {
                if (o1.likeCount == o2.likeCount) {
                    if (o1.emptyCount == o2.emptyCount) {
                        if (o1.y == o2.y) {
                            return o1.x - o2.x;
                        }
                        return o1.y - o2.y;
                    }
                    return o2.emptyCount - o1.emptyCount;
                }
                return o2.likeCount - o1.likeCount;
            }
        });

        // 자리 배정
        for (Seat seat : seats) {
            if (classRoom[seat.x][seat.y] != 0) {
                continue;
            }
            classRoom[seat.x][seat.y] = studentNumber;
            return;
        }
    }

    private static void calculateScore() {
        for (int x = 0; x < N; x++) {
            for (int y = 0; y < N; y++) {
                int count = 0;
                int[] friends = map.get(classRoom[x][y]);

                for (int i = 0; i < 4; i++) {
                    int nx = x + dx[i];
                    int ny = y + dy[i];

                    if (nx < 0 || nx >= N || ny < 0 || ny >= N) {
                        continue;
                    }

                    for (int j = 0; j < 4; j++) {
                        int friend = friends[j];
                        if (classRoom[nx][ny] == friend) {
                            count++;
                        }
                    }
                }

                if (count == 1) {
                    result += 1;
                } else if (count == 2) {
                    result += 10;
                } else if (count == 3) {
                    result += 100;
                } else if (count == 4) {
                    result += 1000;
                }
            }
        }
    }
}

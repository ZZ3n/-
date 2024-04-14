import java.io.*;
import java.util.*;

public class Jun2 {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(bf.readLine());
        int[] numbers = new int[N + 1];
        StringTokenizer stk = new StringTokenizer(bf.readLine());

        for (int i = 1; i <= N; i++) {
            numbers[i] = Integer.parseInt(stk.nextToken());
        }

        stk = new StringTokenizer(bf.readLine());
        int B = Integer.parseInt(stk.nextToken());
        int C = Integer.parseInt(stk.nextToken());

        long result = 0;
        result += N;    // 모든 시험장에 총 감독관 투입

        for (int i = 1; i <= N; i++) {
            int number = numbers[i];
            number -= B;    // 응시자 수에서 총 감독관이 감시 가능한 인원 수를 뺌

            if (number <= 0) {  // 총 감독관이 모든 응시자를 감시할 수 있는 경우
                continue;
            }
            result += (number % C != 0 ? number / C + 1 : number / C);
        }

        System.out.print(result);
    }
}

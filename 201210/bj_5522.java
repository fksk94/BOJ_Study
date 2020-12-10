import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int sum = 0;
		for (int i = 0; i < 5; i++) {
			String[] S = bf.readLine().split(" ");
			int N = Integer.valueOf(S[0]);
			sum = N + sum;
		}
		System.out.println(sum);
	}
}
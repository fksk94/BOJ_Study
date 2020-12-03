import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] S = bf.readLine().split(" ");
		int N = Integer.valueOf(S[0]);
		int M = Integer.valueOf(S[1]);
		int real_res = (N-1) + (M-1)*N;
		System.out.println(real_res);
	}
}
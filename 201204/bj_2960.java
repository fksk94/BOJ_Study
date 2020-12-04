import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] S = bf.readLine().split(" ");
		int N = Integer.valueOf(S[0]);
		int M = Integer.valueOf(S[1]);
		ArrayList<String> arr = new ArrayList<>(N-1);
		ArrayList<String> del = new ArrayList<>(M);
		for (int i = 2; i < N+1; i++) {
			arr.add(Integer.toString(i));
		}
		while (true) {
			int tmp = Integer.valueOf(arr.get(0));
			for (int i = tmp; i<N+1; i=i+tmp) {
				if (arr.remove(Integer.toString(i))) {
					del.add(Integer.toString(i));
				}
			}
			if (del.size() >= M) {
				break;
			}
		}
		System.out.println(del.get(M-1));
	}
}
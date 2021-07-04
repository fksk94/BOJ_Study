import java.io.*;

public class Main {
	public static boolean[] visit = new boolean[9];
	public static int[] a = new int[7];
	
	public static int comb(int[] arr, int[] ans, int n, int cnt) {
		if (cnt == 7) {
			if (n == 100) {
				int j = 0;
				while (j < a.length) {
					a[j] = ans[j];
					j++;
				}
			}
			return 0;
		}
		for (int i = 0; i < arr.length; i++) {
			if (visit[i] == false) {
				visit[i] = true;
				ans[cnt] = arr[i];
				comb(arr, ans, n + arr[i], cnt + 1);
				visit[i] = false;
			}
		}
		return 0;
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		int[] arr = new int[9];
		int[] tmp = new int[7];
		int i = 0;
		while (i < 9) {
			arr[i] = Integer.parseInt(bf.readLine());
			visit[i] = false;
			i++;
		}
		comb(arr, tmp, 0, 0);
		i = 0;
		while (i < a.length) {
			System.out.println(a[i]);
			i++;
		}
	}
}
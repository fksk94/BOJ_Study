import java.util.*;
import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String S = bf.readLine();
		int N = Integer.valueOf(S);
		List<String> stack = new ArrayList<String>();
		for (int i = 0; i < N; i++) {
			String[] line = bf.readLine().split(" ");
			if (line[0].equals("push")) {
				stack.add(line[1]);
			} else if (line[0].equals("top")) {
				if (stack.size() == 0) {
					System.out.println(-1);
				} else {
					System.out.println(stack.get(stack.size()-1));
				}
			} else if (line[0].equals("pop")) {
				if (stack.size() == 0) {
					System.out.println(-1);
				} else {
					System.out.println(stack.get(stack.size()-1));
					stack.remove(stack.size()-1);
				}
			} else if (line[0].equals("empty")) {
				if (stack.size() == 0) {
					System.out.println(1);
				} else {
					System.out.println(0);
				}
			} else {
				System.out.println(stack.size());
			}
		}
	}
}
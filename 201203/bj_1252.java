import java.io.*;
import java.math.BigInteger;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] S = bf.readLine().split(" ");
		BigInteger N = new BigInteger(S[0], 2);
		BigInteger M = new BigInteger(S[1], 2);
		String real_res = N.add(M).toString(2);
		System.out.println(real_res);
	}
}
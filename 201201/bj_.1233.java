import java.io.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] line = bf.readLine().split(" ");
		int[] arr = new int[Integer.valueOf(line[0])+ Integer.valueOf(line[1])+ Integer.valueOf(line[2])+1];
		for (int i = 1; i <= Integer.valueOf(line[0]); i++) {
			for (int j = 1; j <= Integer.valueOf(line[1]); j++) {
				for (int z = 1; z <= Integer.valueOf(line[2]); z++) {
					arr[i+j+z]++;
				}
			}
		}
		int max = arr[0];
		int idx = 0;
		for(int i=1 ; i<arr.length ; i++){
			if(arr[i] > max){
				max = arr[i];
				idx = i;
			}
		}
	    System.out.println(idx);
	}
}
/**
import java.util.*;
import java.io.*;
import java.math.BigInteger;

public class Main {
	static int ans;
	static int answer = 0;
	static ArrayList<Integer> a; 
	
	public static void main(String[] args) throws IOException {
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] P = bf.readLine().split(" ");
		int len = Integer.parseInt(P[0]);
		int res = Integer.parseInt(P[1]);
		ans = res;
		String[] S = bf.readLine().split(" ");
		ArrayList<Integer> arr = new ArrayList<>();
		ArrayList<Integer> stack = new ArrayList<>();
		for(int i = 0; i < len; i++) {
			arr.add(Integer.parseInt(S[i]));
		}
		a = arr;
		for(int i = 0; i < len; i++) {
			stack.add(arr.get(i));
			dfs(stack, i, len);
			stack.remove(0);
		}
		System.out.println(answer);
	}
	
	public static void dfs(ArrayList<Integer> arr, int x, int len) {
		for(int i = x + 1; i < len; i++) {
			arr.add(a.get(i));
			if (arr.size()%2 == 0 && ans == sum(arr)) {
				answer += 1;
			}
			dfs(arr, i, len);
			arr.remove(i);
		}
	}
	
	public static int sum(ArrayList<Integer> arr) {
		int res = 0;
		for(int i = 0; i < arr.size(); i++) {
			res += arr.get(i);
		}
		return res;
	}
}
**/
// 자바.. 좀 더 공부하기 위해서 인터넷 서치함.. ㅠ

import java.util.Scanner;
 
public class Main {
    static int N, S, count=0;
    static int[] arr;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N= sc.nextInt();
        S= sc.nextInt();
        arr = new int[N];
        for (int i = 0; i <N ; i++) {
            arr[i] =  sc.nextInt();
        }
 
        dfs(0,0);
 
        if(S==0){
            count--;
            System.out.println(count);
        }else {
            System.out.println(count);
        }
 
 
    }
 
    private static void dfs(int v , int su){
        if(v==N){
            if(su == S){
                count++;
            }
            return;
        }

        dfs(v+1, su+arr[v]);
        dfs(v+1, su);
    }
}
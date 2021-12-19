import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        double D = Integer.parseInt(s[0]);
        double H = Integer.parseInt(s[1]);
        double W = Integer.parseInt(s[2]);
        double div = Math.sqrt(D * D / (H * H + W * W));

        System.out.println((int)Math.floor(H * div) + " " + (int)Math.floor(W * div));

    }
}
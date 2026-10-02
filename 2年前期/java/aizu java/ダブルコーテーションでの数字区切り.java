import java.util.Scanner;

public class Program {
    int n;

    public void input() {
        Scanner scan = new Scanner(System.in);
        n = scan.nextInt();
        scan.close();
    }

    public void compute() {
        // 必要な計算をここに追加します
    }

    public void output() {
        if (n >= 1000) {
            System.out.println((n / 1000) + "" + ((n / 100) % 10) + "-" + ((n / 10) % 10) + "" + (n % 10));
        } else if (n >= 100) {
            System.out.println("." + (n / 100) + " " + ((n / 10) % 10) + "" + (n % 10));
        } else if (n >= 10) {
            System.out.println("." + "." + " " + (n / 10) + "" + (n % 10));
        } else {
            System.out.println("." + "." + " " + "." + n);
        }
    }

    public static void main(String[] args) {
        Program p = new Program();
        p.input();
        p.compute();
        p.output();
    }
}
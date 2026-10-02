import java.util.Scanner;

public class Program {
    int i = 0, x = 0, avg, count = 0;

    public void input() {
        Scanner scan = new Scanner(System.in);
        while (true) {
            i = scan.nextInt();
            if (i == -1) {
                break;
            }
            x += i;
            count++;
        }
    }

    public void compute() {
        if (count > 0) {
            avg = x / count; 
        }
    }

    public void output() {
        System.out.println(avg);
    }

    public static void main(String[] args) {
        Program p = new Program();
        p.input();
        p.compute();
        p.output();
    }
}

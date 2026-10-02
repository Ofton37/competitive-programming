
import java.util.Random;
public class Program {
 int imax, n;
 double x, y;
 
 public void compute() {
  n = 0;
  imax = 10000000;
  Random rand = new Random();

  for (int i = 0; i <= imax; i++) {
   x = rand.nextDouble();
   y = rand.nextDouble();

   if ((x*x + y*y) < 1.0) {
    n++;
   }
  }
 }
 public void output() {
   System.out.println((double)n /  imax * 4.0);
 }

 public static void main(String[] args) {
  Program p = new Program();
  p.compute();
  p.output();
 }
}
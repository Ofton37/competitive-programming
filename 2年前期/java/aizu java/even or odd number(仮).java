public class Program {
 public void output() {
  int n = 10;

  if (n % 2 == 0) {
   System.out.println(n + " is even number.");
  } else {
   System.out.println(n + " is odd number.");
  }
 }
 public static void main(String[] args) {
  Program p = new Program();
  p.output();
 }
}
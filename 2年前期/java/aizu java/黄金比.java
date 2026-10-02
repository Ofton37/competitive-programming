public class Program {
 public double compute(int count) {
  if (count > 20) {
   return 1.0;
  } else {
   return (1 + (1 / compute(++count)));
  }
 }

 public void output() {
   System.out.println(compute(1));
 }

 public static void main(String[] args) {
  Program p = new Program();
  p.output();
 }
}
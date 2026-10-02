
import java.util.Scanner;
public class Program{

 public void input(){
  Scanner scan = new Scanner(System.in);
 }

 public void compute(){
 }

 public void output(){
  int a, b, c;
  double re1, re2 = 0, im1, im2 = 0, D;

  a = 2;
  b = -5;
  c = 2;
  D = b * b - 4 * a * c;
  if (D > 0) {
   re1 = (-b + Math.sqrt(D)) / (2 * a);
   re2 = (-b - Math.sqrt(D)) / (2 * a);
   im1 = 0;
   im2 = 0;
  } else if (D == 0) {
   re1 = -b / (2 * a);
   im1 = 0;
  } else {
   re1 = re2 = -b / (2 * a);
   im1 =  im2 = Math.sqrt(-D) / (2 * a);
  } 
  if (D == 0) {
   System.out.println("x = " + re1 + " + " + im1 + "i");
  } else {
  System.out.println("x = " + re1 + " + " + im1 + "i, " + re2 + " + " + im2 + "i");
  }
 }

 public static void main(String[] args) {
  Program p = new Program();
  p.input();
  p.compute();
  p.output();
 }
}
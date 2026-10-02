import java.util.Scanner;
public class Program{

 public void input(){
  Scanner scan = new Scanner(System.in);
 }

 public void compute(){
 }

 public void output(){
  int[][] A = {{1,2},{-2,-5}};
  double detA = A[0][0] * A[1][1] - A[0][1] * A[1][0];
  if (detA == 0) {
   System.out.println("X");
  } else {
   System.out.println(1/detA*A[1][1] + " " + 1/detA*(-A[0][1]));
   System.out.println(1/detA*(-A[1][0]) + " " + 1/detA*A[0][0]);
  }
 }

 public static void main(String[] args) {
  Program p = new Program();
  p.input();
  p.compute();
  p.output();
 }
}
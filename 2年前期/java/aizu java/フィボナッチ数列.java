import java.util.Scanner;
public class Program{

 public void input(){
  Scanner scan = new Scanner(System.in);
 }

 public void compute(){
 }

 public void output(){
  int n = 20;
  int a_n_1 = 1;
  int a_n_2 = 1;
  System.out.println(a_n_2); 
  System.out.println(a_n_1);
  for (int i = 2; i < n; i++) {
   int a_n = a_n_1 + a_n_2;
  System.out.println(a_n);
  a_n_2 = a_n_1;
  a_n_1 = a_n;
  }
 }

 public static void main(String[] args) {
  Program p = new Program();
  p.input();
  p.compute();
  p.output();
 }
}
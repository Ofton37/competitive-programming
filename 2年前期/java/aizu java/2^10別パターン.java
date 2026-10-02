import java.util.Scanner;
public class Program{

 public void input(){
  Scanner scan = new Scanner(System.in);
 }

 public void compute(){
 }

 public void output(){
  int sum = 1;
  for (int i = 0; i < 10; i++) {
   sum *= 2;
  }
  System.out.println(sum);
 }

 public static void main(String[] args) {
  Program p = new Program();
  p.input();
  p.compute();
  p.output();
 }
}
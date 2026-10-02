import java.util.Scanner;
public class Program{
 int n1,n2,n3,n4,n5,i = 0;

 public void input(){
  Scanner scan = new Scanner(System.in);
  n1 = scan.nextInt();
  n2 = scan.nextInt();
  n3 = scan.nextInt();
  n4 = scan.nextInt();
  n5 = scan.nextInt();
  scan.close();
 }

 public void compute(){
  if (n1 > 0) i++;
  if (n2 > 0) i++;
  if (n3 > 0) i++;
  if (n4 > 0) i++;
  if (n5 > 0) i++;
 }

 public void output(){
  System.out.println(i);
 }

 public static void main(String[] args) {
  Program p = new Program();
  p.input();
  p.compute();
  p.output();
 }
}
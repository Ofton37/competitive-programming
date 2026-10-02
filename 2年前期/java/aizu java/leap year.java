import java.util.Scanner;
public class Program{

 public void input(){
  Scanner scan = new Scanner(System.in);
 }

 public void compute(){
 }

 public void output(){
  int year = 2012;
  if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
   System.out.println(year + " is a leap year."); 
  } else {
   System.out.println(year + " is not a leap year."); 
  }
 }

 public static void main(String[] args) {
  Program p = new Program();
  p.input();
  p.compute();
  p.output();
 }
}
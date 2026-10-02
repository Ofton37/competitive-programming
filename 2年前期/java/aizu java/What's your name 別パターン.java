
import java.util.Scanner;
public class Program{

 public void input(){
  Scanner scan = new Scanner(System.in);
 }

 public void compute(){
 }

 public void output(){
  String s = "Aizu Taro";
  System.out.println("Hello, " + s + ". How are you?");
 }

 public static void main(String[] args) {
  Program p = new Program();
  p.input();
  p.compute();
  p.output();
 }
}
public class Program {
 public void output() {
  String s = "fine";

  if (s == "fine") {
   System.out.println("That's good!");
  } else if (s == "rain") {
   System.out.println("That's bad");
  }
 }
 public static void main(String[] args) {
  Program p = new Program();
  p.output();
 }
}
public class Intro{
  int x=5;
  String car="lamb";
  public Intro(String car){
    this.car=car;
  }
  public static void main(String[] args) {
    Intro intro=new Intro("was");
    System.out.println(intro.car);
  }
}
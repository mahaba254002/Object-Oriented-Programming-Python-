public class self_this {
  private double radius;

  public self_this(double radius) {
    this.radius = radius;
  }

  public double calculateArea() {
    double area = 3.14 * this.radius * this.radius;
    return area;
  }

  public double calculateCircumference() {
    double circumference = 2 * 3.14 * this.radius;
    return circumference;
  }

  public static void main(String[] args) {
    self_this myCircle = new self_this(5);
    System.out.println(myCircle.calculateArea());
    System.out.println(myCircle.calculateCircumference());
  }
}
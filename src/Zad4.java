import java.util.Stack;
public class Zad4 {
    public static int ONP(String expre) {
        Stack<Integer> s = new Stack<>();
        String[] znaki = expre.split(" ");
        int a;
        int b;
        for (String current : znaki) {

            if (!(current.equals("/")) && !(current.equals("+")) && !(current.equals("*")) && !(current.equals("-"))) {
                s.push(Integer.parseInt(current));
            }
            switch (current) {
                case "+" -> {
                    a = s.pop();
                    b = s.pop();
                    s.push(a + b);
                }
                case "-" -> {
                    a = s.pop();
                    b = s.pop();
                    s.push(b - a);
                }
                case "*" -> {
                    a = s.pop();
                    b = s.pop();
                    s.push(a * b);
                }
                case "/" -> {
                    a = s.pop();
                    b = s.pop();
                    s.push(b / a);
                }
            }
        }
        return s.pop();
    }
}

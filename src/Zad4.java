import java.util.Stack;
public class Zad4 {
    public static int ONP(String expre) {
        Stack<Integer> s = new Stack<>();
        String[] znaki = expre.split(" ");
        int a;
        int b;
        for (int i = 0; i < znaki.length; i++) {
            String current = znaki[i];

            if (!(current.equals("/")) && !(current.equals("+")) && !(current.equals("*")) && !(current.equals("-"))) {
                s.push(Integer.parseInt(current));
            }
            switch (current) {
                case "+":
                    a = s.pop();
                    b = s.pop();
                    s.push(a + b);
                    break;

                case "-":
                    a = s.pop();
                    b = s.pop();
                    s.push(b - a);
                    break;

                case "*":
                    a = s.pop();
                    b = s.pop();
                    s.push(a * b);
                    break;

                case "/":
                    a = s.pop();
                    b = s.pop();
                    s.push(b / a);
                    break;

            }
        }
        return s.pop();
    }
}

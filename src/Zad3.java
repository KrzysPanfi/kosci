import java.util.Stack;
public class Zad3 {
    public static String odwrocone_znaki(String exp) {
        Stack<Character> stack = new Stack<>();
        char[] znaki = exp.toCharArray();
        char[] odwrocone_znaki = new char[znaki.length];
        for (int i = 0; i < znaki.length; i++) {
            stack.push(znaki[i]);
        }
        for (int j = 0; j < znaki.length; j++) {
            odwrocone_znaki[j] = stack.pop();
        }

        return new String(odwrocone_znaki);
    }
}

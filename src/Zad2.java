import java.util.Stack;

public class Zad2 {
    public static boolean balancedParenthesis(String expr) {

        Stack<Character> stack = new Stack<>();

        char[] znaki = expr.toCharArray();

        for (int i = 0; i < znaki.length; i++) {

            char current = znaki[i];

            if (current == '{' || current == '[' || current == '(') {
                stack.push(current);
            }
            char popChar;
            switch (current) {
                case ')':
                    popChar = stack.pop();
                    if (popChar == '{' || popChar == '[')
                        return false;
                    break;
                case '}':
                    popChar = stack.pop();
                    if (popChar == '(' || popChar == '[')
                        return false;
                    break;
                case ']':
                    popChar = stack.pop();
                    if (popChar == '(' || popChar == '{')
                        return false;
                    break;
            }
        }
        return stack.empty();

    }
}

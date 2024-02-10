import java.util.Stack;

public class Zad2 {
    public static boolean balancedParenthesis(String expr) {

        Stack<Character> stack = new Stack<>();

        char[] znaki = expr.toCharArray();

        for (char current : znaki) {

            if (current == '{' || current == '[' || current == '(') {
                stack.push(current);
            }
            char popChar;
            switch (current) {
                case ')' -> {
                    popChar = stack.pop();
                    if (popChar == '{' || popChar == '[')
                        return false;
                }
                case '}' -> {
                    popChar = stack.pop();
                    if (popChar == '(' || popChar == '[')
                        return false;
                }
                case ']' -> {
                    popChar = stack.pop();
                    if (popChar == '(' || popChar == '{')
                        return false;
                }
            }
        }
        return stack.empty();

    }
}

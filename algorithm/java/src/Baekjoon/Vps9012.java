package Baekjoon;

import java.util.Scanner;
import java.util.Stack;

public class Vps9012 {
    /*
        괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
        그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
        한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다.
        만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다.
        그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
        예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.
        여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.

        입력 데이터는 표준 입력을 사용한다.
        입력은 T개의 테스트 데이터로 주어진다.
        입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
        각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다.
        하나의 괄호 문자열의 길이는 2 이상 50 이하이다.

        출력은 표준 출력을 사용한다.
        만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.


        스택을 사용하면 어렵지 않지만, 스택을 써야겠다는 생각을 하는것이 쉽지 않은 것 같다.
        문제를 보고 어떤 핵심 기능을 써야할 지 딱 튀어나올 정도로 숙달을 해줘야 할 것 같다.
     */

    public static void main(String[] args){
        // 정수 하나 놓고 (면 쁘라스 하고 )면 마이나스 해서 0이면 YES 하면 되는거 아닌가?
        // 아니다. 이러면 )(도 오케이가 된다. ())()(()도 오케이가 된다.
        // 규칙을 어떻게 해야하지?
        // 스택에 (면 푸시하고 )면 팝해서 문제 생기면 NO 하면 되는건가?
        // 해보면 될 듯?
        // 됐다!
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();
        String[] psArr = new String[n];
        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < psArr.length; i++){
            psArr[i] = sc.nextLine();
        }

        for(String ps : psArr){
            /*
                기본값은 YES.
                입력받은 값이
                1. '('일 때 push,
                2. ')'일 때 empty 확인해서 비어있으면( ')'와 매칭될 '('가 없다는 뜻 = 잘못됨 ) NO 반환. 비어있지 않으면 pop.
                3. 마지막으로 스택이 비어있지 않으면( '('와 매칭될 ')'가 없다는 뜻 = 잘못됨 ) NO 반환.
             */
            String res = "YES";

            char[] chars = ps.toCharArray();
            for(char c : chars){
                if(c == '('){
                    stack.push(c);
                }else{
                    if(stack.isEmpty()){
                        // ()())
                        res = "NO";
                        break;
                    }else{
                        stack.pop();
                    }
                }
            }

            // ()()(
            if(!stack.isEmpty()){
                res = "NO";
            }

            stack.clear();
            System.out.println(res);
        }
    }
}
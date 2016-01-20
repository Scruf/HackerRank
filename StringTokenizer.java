    
import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
            Scanner scan = new Scanner(System.in);
        String str = scan.nextLine();
        StringTokenizer m = new StringTokenizer(str,"[!,?.\\_'@ ]+");
        System.out.println(m.countTokens());
        while(m.hasMoreTokens()){
            System.out.println(m.nextToken());
        }
    }
}

import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    static String isPrime(int number){
       if (number <= 1) {
       return "Not prime";
   }
   for (int i = 2; i < Math.sqrt(number); i++) {
       if (number % i == 0) {
           return "Not prime";
       }
   }
   return "Prime";
    }
    public static void main(String[] args) {
        Scanner scan  = new Scanner(System.in);
        int T = scan.nextInt();
        for(int i=0;i<T;i++){
            int number=scan.nextInt();
            String prime = isPrime(number);
            System.out.println(prime);
        }
    }
}

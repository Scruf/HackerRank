import java.io.*;
import java.util.*;
public class Solution {
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
     
        int gcd=find_gcd(a,b);
        System.out.println(gcd);
    }
   static  int find_gcd(int a,int b){
         if(a==b)
             return a;
        else
           {
            if(a%b==0)
                return b;
            else
                return find_gcd(b,a%b);
        }
         
      }
}
 

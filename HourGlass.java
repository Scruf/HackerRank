/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package hourglass;

/**
 *
 * @author ekozi
 */
import java.util.Scanner;
public class HourGlass {
   
    public static void main(String[] args) {
       Scanner in = new Scanner(System.in);
        int arr[][] = new int[6][6];
        for(int i=0; i < 6; i++){
            for(int j=0; j < 6; j++){
                arr[i][j] = in.nextInt();
            }
        }
        int c=0,d = Integer.MIN_VALUE;
         for(int i=1; i < 5; i++){
        for(int j=1; j < 5; j++){
          c=arr[i][j]+arr[i-1][j-1]+arr[i-1][j]+arr[i-1][j+1]+arr[i+1][j-1]+arr[i+1][j]+arr[i+1][j+1];
        if(d<=c){d=c;}
        }

    }
        System.out.println(d);
    }
    
}

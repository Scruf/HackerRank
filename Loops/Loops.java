/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package loops;

/**
 *
 * @author Kozitski
 */
import java.util.Scanner;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
public class Loops {

    /**
     * @param args the command line arguments
     */
    static int sumReturn(int numb,int multiplayer){
        int sum=0;
             if(numb==0)
                    return multiplayer;
                for(int j=0;j<=numb;j++){
                    sum=sum+((int)Math.pow(2, j)*multiplayer);
                }
                
            return sum;
        
    }
    public static void main(String[] args) {
      Scanner scan  = new Scanner(System.in);
      List<Integer>numbers = new ArrayList<Integer>();
      Map<Integer,List<Integer>> map = new HashMap<>();
      
        int testCase = scan.nextInt();
      for(int i=0;i<testCase;i++){
         //get the string of numbers
        
          Scanner scanString = new Scanner(System.in);
          String str = " ";
          while(scanString.hasNextLine()){
              str = scanString.nextLine();
          }
    
          int multiplayer = Integer.parseInt(str.split(" ")[1]);
         
          int length = Integer.parseInt(str.split(" ")[2]);
          
          for(int j=0;j<length;j++){
              int sum = Integer.parseInt(str.split(" ")[0])+sumReturn(j,multiplayer);
            
              numbers.add(sum);
          }
     
          map.put(i, numbers);
        numbers = new ArrayList<Integer>();
          
        }
        for(int i=0;i<testCase;i++){
           List<Integer> list = map.get(i);
           for(Integer x : list){
               System.out.print(x+" ");
           }
           System.out.println();
        }
      }
    }
    


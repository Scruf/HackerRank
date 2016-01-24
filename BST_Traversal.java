import java.io.*;
import java.util.*;
class Node{
    Node left,right;
    int data;
    Node(int data){
        this.data=data;
        left=right=null;
    }
}
class Solution{
    static void levelOrder(Node root){
        if(root==null)
            return;
        else{
            Queue<Node> q  = new LinkedList<Node>();
            q.add(root);
            while(q.peek()!=null){
                Node temp = q.remove();
                System.out.print(temp.data+" ");
                if(temp.left!=null)
                    q.add(temp.left);
                if(temp.right!=null)
                    q.add(temp.right);
            }
        }
         
       
      
    }
    static void levelOrder(Node root){
        if(root==null)
            return;
        else{
            Queue<Node> q  = new LinkedList<Node>();
            q.add(root);
            while(q.peek()!=null){
                Node temp = q.remove();
                System.out.print(temp.data+" ");
                if(temp.left!=null)
                    q.add(temp.left);
                if(temp.right!=null)
                    q.add(temp.right);
            }
        }
         
       
      
    }

public class Day6 {

    /**
     * @param args the command line arguments
     */
 
    public static void main(String[] args) {
          Scanner in = new Scanner(System.in);
             int n = in.nextInt();
             ArrayList<String> list = new ArrayList<String>(n);
          for(int i=0;i<n;i++){
              list.add(" ");
          }
           
             for(int i=list.size()-1;i>=0;i--){
                 list.set(i, "#");
                 for(String s : list)
                     System.out.print(s);
                 System.out.println();
             }
     }

   public static void main(String[] args) {
         Scanner scan = new Scanner(System.in);
        Scanner numberScan = new Scanner(System.in);
        
        int numbOfTestCase = scan.nextInt();
        String []arr = new String [numbOfTestCase];
        for(int i=0;i<numbOfTestCase;i++){
             int number=0;
             if(numberScan.hasNextLine())
                  number = numberScan.nextInt();
          
         
            arr[i]=Integer.toBinaryString(number);
          
        }
        for(String s : arr){
            System.out.println(s);
        }
    }

package meet06;

public class Main {

    public static int countNegs (int [][] mat){
        int count = 0;
        for (int [] row : mat)
            for (int num : row)
                if (num < 0)
                    count++;
        return count;
    }

    // public static int countEven(int[] arr) {

    //     int count = 0;
    //     for (int num : arr){
    //         if(num%2 == 0){
    //             count++;   
    //         }
    //     }
    //     return count;
    // }
    // public static void changeEven(int[] arr) {
    //     for (int i = 0; i < arr.length; i += 2)
    //         arr[i] = 0;

    // }

    // public static int findMin (int[] arr){
    //     int min = arr[0];
    //     int minIndex = 0;
    //     for(int i = 1; i < arr.length; i++)
    //         if(arr[1] < min)
    //         {
    //             min = arr[i];
    //             minIndex = i;
    //         }
    //     return minIndex;
    // }
    // public static int findMax(int[] arr) {
    //     int max = arr[0];
    //     int maxIndex = 0;
    //     for (int i = 1; i < arr.length; i++) { 
    //         if (arr[i] > max) { 
    //             max = arr[i];
    //             maxIndex = i;
    //         }
    //     }
    //     return maxIndex;
    // }


    public static void main(String[] args) {
    //     int[] coins = new int[4];
    //     coins[0] = 1;
    //     coins[1] = 5;
    //     coins[2] = 10;
    //     coins[3] = 25;

    //     String[] names = {"p", "a", "k"};

    //     for (int coin : coins) {
    //         System.out.printf(coin+" ");
    //     }
    //     System.out.println();

    //     for (int i = 0; i < names.length; i++) {
    //         System.out.printf(names[i]+ " ");
    //     }
    //     System.out.println();

    //     System.out.println(countEven(coins));
    //     changeEven(coins);
    //     for (int coin : coins) {
    //         System.out.printf(coin+" ");
    //     }

    //     System.out.println();

    //     System.out.println(coins[findMax(coins)]);

    //     System.out.println(coins[findMin(coins)]);
        
    // 
    // Deck d = new Deck();
    // d.shuffle();
    // d.writeDeck();

    // Manydecks d = new Manydecks();
    // d.shuffleAll();
    // d.printDecks();

    // ArrayList = {0, 1, 4, 9}
    // List<Integer> list = new ArrayList<Integer>();
    // for (int i = 0; i < 4; i++)
    //     list.add(i * i);

    // Integer intOb = list.get(2);

    // int n = list.get(3);

    // Integer x = list.set(3, 5);
    
    // x = list.remove(2);

    // list.add(1, 7);
    // list.add(2, 8);
    // 

     int [] [] table;

    double[][] matrix = new double[3][4];

    String[] [] strs = new String [2] [5];

    int [] [] mat = { {3, 4, 5}, 
                        {6, 7, 8}};
                                 
    }

}

import java.lang.*;
import java.io.*;
import java.util.*;

public class PathFinder{

    public static long PF_helper(int n){

        long[][] matrix = new long[n][n];

        for (int i = 0; i < n; i ++) {
            for (int j = 0; j < n; j ++) {
                matrix[i][j] = 0;
            }
        }

        for (int i = 0; i < n; i ++) {
            matrix[n-1][i] = 1;
        }

        for (int r = n - 2; r >= 0; r --) {
            for (int c = n - r - 1; c < n; c ++) {
                matrix[r][c] = matrix[r][c-1] + matrix[r+1][c];
            }
        }

        return matrix[0][n-1];

    }
    public static void main(String[] argv) {
        int n;
        while (true) {
            
            Scanner console = new Scanner(System.in);
            System.out.println("Please enter size: ");
            n = console.nextInt();
            long way = PF_helper(n);
            System.out.println("There are " + way + " ways to get from A to B.");
        }

    }

}

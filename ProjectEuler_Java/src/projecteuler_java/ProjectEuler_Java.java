/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package projecteuler_java;

import static java.lang.Math.abs;
import static java.lang.Math.floor;
import static java.lang.Math.sqrt;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 *
 * @author Ronnie
 */
public class ProjectEuler_Java {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        /**
         * Project Euler problem 3: Largest prime factor
         * The prime factors of 13195 are 5, 7, 13 and 29.
         * What is the largest prime factor of the number 600851475143 ?
         */
        System.out.println("Hello World");
        double myNum; // needs to be a double as it is a very large number
        System.out.println(6.0 % 4);
        
        myNum = 600851475143.0;
        largestPrimeFactor(myNum); // Find largest prime
                
    }
    
    public static boolean isPrime(double x){
        //number must be round and greater than 1
        
        
        if ((floor(x) < 2)|(abs(x % 1) > 0.00001)){
            return false;
        }
                
        // Checks primality by simple trial division
        for(int i = 2; i < sqrt(x); i++){
            if (floor(x) % i == 0){
                return false;
            }
        }
        return true;
    }
    
    public static double largestPrimeFactor(double x){
        System.out.println(x);
        List myFactors = new ArrayList();
        
        int index;
        index = 0;
        int j;
        
        x = floor(x);
        
        for(int i = 2; i < sqrt(x); i++){
            if (x % i < 0.0001){
                // x = i * j. Add to list of factors
                myFactors.add(i);
                j = (int) (x / i);
                myFactors.add(j);
                index += 2;
            }
        }
        
        // Print factors array
        System.out.println(myFactors);
        
        List primeFactors = new ArrayList();
        // Check if a factor is prime
        for(int i = 0; i < myFactors.size(); i++){
            if (isPrime(myFactors.get(i))){
                primeFactors.add(myFactors.get(i));
            }
        }
        return max(primeFactors);
    }

    private static double max(int[] myArray) {
        int maxVal = 0; // we are assuming at least one positive value in the array
        for(int i=0; i<myArray.length; i++){
            if(myArray[i]>maxVal){
                maxVal = myArray[i];
            }
        }
        return maxVal;
    }
    
    
}

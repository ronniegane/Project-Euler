/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package projecteuler_java;

import static java.lang.Math.abs;
import static java.lang.Math.floor;

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
        for(int i = 2; i < java.lang.Math.sqrt(x); i++){
            if (floor(x) % i == 0){
                return false;
            }
        }
        return true;
    }
    
    public static double largestPrimeFactor(double x){
        System.out.println(x);
        // Work out all factors
        // Check if a factor is prime
        return 1.0;
    }
    
    
}

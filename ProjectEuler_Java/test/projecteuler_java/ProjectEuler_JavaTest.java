/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package projecteuler_java;

import org.junit.AfterClass;
import org.junit.BeforeClass;
import org.junit.Test;
import static org.junit.Assert.*;

/**
 *
 * @author Ronnie
 */
public class ProjectEuler_JavaTest {
    
    public ProjectEuler_JavaTest() {
    }
    
    @BeforeClass
    public static void setUpClass() {
    }
    
    @AfterClass
    public static void tearDownClass() {
    }

    /**
     * Test of main method, of class ProjectEuler_Java.
     */
    @Test
    public void testMain() {
        System.out.println("main");
        String[] args = null;
        ProjectEuler_Java.main(args);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }

    /**
     * Test of isPrime method, of class ProjectEuler_Java.
     */
    @Test
    public void testIsPrime() {
        System.out.println("isPrime");
        //check edge cases
        
        assertFalse("Testing primality of 0",ProjectEuler_Java.isPrime(0));
        assertFalse("Testing primality of 1",ProjectEuler_Java.isPrime(1));
        
        //check known primes and non-primes
        assertFalse("Testing primality of 55", ProjectEuler_Java.isPrime(55));
        assertTrue("Testing primality of 7", ProjectEuler_Java.isPrime(7));
        assertTrue("Testing primality of 173",ProjectEuler_Java.isPrime(173));
        
        //check invalid inputs for exception handling
        assertFalse("Testing non-integer input", ProjectEuler_Java.isPrime(3.3));
        String myString;
        myString = "abc";
        //assertEquals(false,ProjectEuler_Java.isPrime(myString));

    }

    /**
     * Test of largestPrimeFactor method, of class ProjectEuler_Java.
     */
    @Test
    public void testLargestPrimeFactor() {
        System.out.println("largestPrimeFactor");
        assertEquals("Prime factor of 12", 3, ProjectEuler_Java.largestPrimeFactor(12), 0.0001);
        assertEquals("Prime factor of 2", 2, ProjectEuler_Java.largestPrimeFactor(2), 0.0001);
        assertEquals("Prime factor of 17", 17, ProjectEuler_Java.largestPrimeFactor(17), 0.0001);        
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    
}

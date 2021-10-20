// Instructions 

// Fix the function
// I created this function to add five to any number that was passed in to it and return the new value. It doesn't throw any errors but it returns the wrong number.

// Can you help me fix the function?

// public class Solution {
//   public static int addFive(int num) {
//     int total = num + 5;
//     return num;
//   }
// }

// Solution

public class Solution {
  public static int addFive(int num) {
    int total = num + 5;
    return total;
  }
}


// Sample Tests

// import org.junit.Test;
// import static org.junit.Assert.assertEquals;
// import org.junit.runners.JUnit4;

// public class SolutionTest {
//     @Test
//     public void testAddFive() {
//       assertEquals(10, Solution.addFive(5));
//     }
//     @Test
//     public void testAddZero() {
//       assertEquals(5, Solution.addFive(0));
//     }
//     @Test
//     public void testAddNegativeFive() {
//       assertEquals(0, Solution.addFive(-5));
//     }
//     @Test
//     public void testRandom() {
//       for (int i = 0; i < 50; i++) {
//         int rand = (int)(Math.random() * 1000) + 1;
//         assertEquals(rand+5, Solution.addFive(rand));
//       }
//     }
// }

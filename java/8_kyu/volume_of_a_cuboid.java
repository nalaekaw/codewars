// Instructions
// Bob needs a fast way to calculate the volume of a cuboid with three values: length, width and the height of the cuboid. Write a function to help Bob with this calculation.


// Solution
public class Kata {

  public static double getVolumeOfCuboid(final double length, final double width, final double height) {
    double cuboid_volume;
    cuboid_volume = length * width * height;
    return cuboid_volume;
  }
  
}

// Tests

// import org.junit.Test;
// import static org.junit.Assert.*;

// public class ExampleTests {

//   private static final double delta = 0.0001;
  
//   @Test
//   public void examples() {
//       // assertEquals("expected", "actual");
//       assertEquals(4, Kata.getVolumeOfCuboid(1, 2, 2), delta);
//       assertEquals(63, Kata.getVolumeOfCuboid(6.3, 2, 5), delta);
//   }
// }

// package howManyStep;

// import static org.junit.jupiter.api.Assertions.assertEquals;
// import org.junit.jupiter.api.Test;
// import org.junit.jupiter.api.DisplayName;

// public class SolutionTest {
    
//     @DisplayName("Random Test Cases")
//     @Test
//     void test() {
//         doTest(1, 10, 4);
//         doTest(1, 17, 5);
//         doTest(1, 64, 6);
//         doTest(1, 63, 10);
//         doTest(50, 100, 1);
//         doTest(51, 100, 49);
//         doTest(100, 100, 0);
//         doTest(462, 5068, 175);

//         for (int i = 0; i < 100; i++) {
//             int aa = (int)(Math.random() * 1000) + 1;
//             int bb = (int)(Math.random() * 9000) + aa;
//             int ans = an(aa, bb);
//             int useran = Kata.howManyStep(aa, bb);
//             assertEquals(ans, useran);
//         }
//     }

//     static int an(int a, int b) {
//         int rs = 0;
//         while (a * 2 <= b) {
//             if (b % 2 != 0) b--;
//             else b /= 2;
//             rs++;
//         }
//         return rs + b - a;
//     }

//     private void doTest(int a, int b, int expected) {
//         int actual = Kata.howManyStep(a, b);
//         assertEquals(actual, expected, "howManyStep(" + a + ", " + b + ")");
//     }
// }

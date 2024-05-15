package exam_score;

import java.util.Arrays;
import java.util.stream.IntStream;

public class Exam {

    public static int checkExam(String[] array1, String[] array2) {
      int[] result = IntStream.range(0, array1.length)
                              .map(i -> {if(array1[i] == array2[i]) return 4;
                                        else if(array2[i] == "") return 0;
                                        else return -1;})
                              .toArray();
      return Arrays.stream(result).sum() < 0 ? 0 : Arrays.stream(result).sum();
    }
  
  }
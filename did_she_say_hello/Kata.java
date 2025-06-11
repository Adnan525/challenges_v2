// You received a whatsup message from an unknown number. 
// Could it be from that girl with a foreign accent you met yesterday evening?
// Write a simple function to check if the string contains the word hallo in different languages
// These are the languages of the possible people you met the night before:
// hello - english
// ciao - italian
// salut - french
// hallo - german
// hola - spanish
// ahoj - czech republic
// czesc - polish
// Note
// you can assume the input is a string.
// to keep this a beginner exercise you don't need to check if the greeting is a subset of word 
// (Hallowen can pass the test)
// function should be case insensitive to pass the tests
// ==============================================================================================
package did_she_say_hello;

import java.util.Arrays;

public class Kata{
  public static boolean validateHello(String greetings){
  /**
  * This function checks if the input string contains any of the greetings in different languages.
  * It returns true if any of the greetings are found, otherwise false.
  *
  * @param greetings The input string to check for greetings.
  * @return boolean True if any greeting is found, false otherwise.
  */
    String[] greetingsList = {"hello", "ciao", "salut", "hallo", "hola", "ahoj", "czesc"};

    return Arrays.asList(greetingsList).stream()
      .anyMatch(greeting -> greetings.toLowerCase().contains(greeting));
  }
  
  public static void main(String[] args) {
    String test = "Hello ciao bella!";
    System.out.println(validateHello(test));
  }
}
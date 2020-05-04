1. Find the Winner!

Andrea and Maria each have a deck of numbered cards in a pile face down. They play a game where they each alternately discard and flip the cards on the pile from top to bottom.

At the beginning of the game, someone will call out "Even" or "Odd". 
The first move depends on which is called. If "Even" is called, the player's top cards are flipped so they can see the face value. If instead "Odd" is called, the top card is removed from each deck and discarded, then each flips her next card. 

Andrea subtracts the value of Maria's card from her own and adds the result to her score. Likewise, Maria subtracts the value of Andrea's card from her own and adds the result to her score. From this point forward, each alternately discards then flips a card. Each time two cards are flipped, the players' scores are computed as before. Once all the cards have been played, whoever has the most points wins.

**As an example:**
Maria's cards, face down, are [3, 5, 6]
Andrea's are [4, 5, 7]. 
After calling "Even" at random, the game begins. 

The following table represents game play with cumulative score at the bottom. 
Maria's score is -2, Andrea's is +2 so Andrea wins.Maria's Andrea's Maria's Andrea'sCard Card Score Score3 4 3 - 4 = -1 4 - 3 = 15 5 Discard Discard6 7 6 - 7 = -1 7 - 6 = 1Cumulative scores -2 2

You must determine the name of the winner if there is one, otherwise they tie.
Return the string Andrea, Maria or Tie as String.

Function DescriptionComplete the function winner in the editor below. The function must return a string denoting the outcome of the game. 
Return Andrea if Andrea won, or return Maria if Maria won. If their scores are tied, return Tie instead. 
Winner has the following parameter(s):
    andrea: An array of n integers that denotes Andrea's array of card values.
    maria: An array of n integers that denotes Maria's array of card values.
    s: A string that represents the starting called out word
    
Constraints2 ≤ n ≤ 1051 ≤ a[i], m[i] ≤ 103, where 0 ≤ i < n
String s will either the word Odd or the word Even.
Input Format For Custom Testing

Sample Case 0
Sample Input: [1,2,3][2,1,3], "Even"
Sample Output 0
MariaExplanation 0
In this game, andrea = [1, 2, 3] and maria = [2, 1, 3]. Because s = Even, the only cards flipped are at indexes 0 and 2.
When i = 0, Andrea gets a[0] − m[0] = 1 − 2 = -1 point and Maria gets m[0] − a[0] = 2 − 1 = 1 point.
When i = 2, Andrea gets a[2] − m[2] = 3 − 3 = 0 points and Maria gets m[2] − a[2] = 3 − 3 = 0 points.
At the end of play, Andrea's cumulative score is -1 and Maria's is 1 so Maria wins.
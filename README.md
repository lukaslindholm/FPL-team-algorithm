Introduction:

The algorithm is based on data from FPL form (https://fplform.com). For each player in the next gameweek, the data contains predicted points, probability of them appearing, and the product of these in separate columns,  
which the site has determined using other data. The FPL price of every player is also included in the data. The algorithm is by no means certain to always find the optimal team based on the data, but it compares the resulting
team to the best team possible without a price limit, from which it can be determined how realistic the result is. From my testing so far, I have found the difference to usually be relatively small.

Algorithm step by step:

1

Filter to only include players with predicted points including prob. of appearance > 2 and prob. of appearance > 0,5 and for each remaining player, create a comparison value consisting of a weighted sum of 
player price and predicted points including prob. of appearance.

2

Sort players in each position according to comparison value, and for midfielders and defenders, take the n best players to decrease later combinations.

3

For each set of players in one position, create all combinations of players according to the required amount from each position in an FPL team, and sort the combinations by combined comparison value.

4

Create an initial best team, using the top combination for each position created in step 3. For n tries, update the best team by the following agorithm:

  - Generate a new team by replacing all the players in one position in the current best team with the next combination in line from that position, created in step 3.
  - Repeat for every posotion in the current best team, and out of the 4 new teams, choose the one whose combined points incl. prob. of appearance is the largest.
  - If the current best team has a price <= 100, check if the next team also has a price <= 100. If so, replace the current best team with the next team if the combined points of the next team is larger.
  - If the current best team is too expensive, replace it with the next team.

After n tries, the resulting team should be a reasonably optimal valid FPL team.

5

Lastly, generate the best possible team without a price limit, and compare the two teams.

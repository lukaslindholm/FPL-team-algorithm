The algorithm is based on data from FPL form (https://fplform.com). For each player in the next gameweek, the data contains predicted points, probability of them appearing, and the product of these in separate columns, which the site has determined using other data. The FPL price of every player is also included in the data. The algorithm is by no means certain to always find the optimal team based on the data, but it compares the resulting team to the best team possible without a price limit, from which it can be determined how realistic the result is. From my testing so far, I have found the difference to usually be small. There are no restriction for the maximum amount of players per team, but the need for this is rare. 

The web scraper allows the data to be replaced automatically, and paired with e.g. task scheduler it can be set to run before every new gameweek. This is mostly a fun project to help me choose my fpl players in a creative way, as well as learning pandas, selenium and improving my coding skills.

Thank you to Nick Hope from FPL Form for allowing me to do this.

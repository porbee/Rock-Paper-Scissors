# Rock paper scissors

I programmed a version of the game **rock paper scissors**.

This version of the game is programmed on *python* and its best played on the terminal. Because it is made for running swiftly on the terminal with visual features that suit it.

The game has three modes which are named on the players win rate of two modalities.

The third modality is just the normal rock paper scissors.

## Modes

The first mode its called *Impossible Mode* because the players win rate is of `0%`.

The second option on the mode selector is *Normal Mode*.

It is the **rock paper scissors** that has an equally random probability of outputting `rock`, `paper` or `scissors`.

The last version of rock paper scissors is *Prediction Mode*.
It is a mode that makes the machine seek and recognize the users playing patterns, trying always to predict what the user is going to play. And reacting accordingly.

## Impossible Mode

It works on *decision trees* that makes the machine always win.

The machine **always wins** because it knows what the user is going to play. 
The decision tree that the machine is based of can be represented as:

```
                                Player
                                INPUT
                               /  |  \
                              /   |   \
                             /    |    \
                         Rock   Paper   Scissors                         
                          |       |        |
                          |       |        |
                          |       |        |
                        Paper  Scissors   Rock
                           \      |       /
                            \     |      /
                             \    |     /
                              \   |    /
                               Machine
                                OUTPUT 
```

It also allows the same words but with difference in the cases
For example: `paper`, `Paper`, `PAPER` and `pAPER` are considered a valid input.

## Normal Mode

It is just the game but the machine's probability of playing different options is completely and equally random. Because the probability of playing any of the three options is of `1/3`.

It doesn't rely on any predicting method because it doesn't want to predict the users answer.

## Prediction Mode

Prediction mode tries to predict the users actions by using probability and memory. The machine learning method that the machine is following is the **Naive Bayes method**[^1].

[^1]: https://en.wikipedia.org/wiki/Naive_Bayes_classifier

It depends on predicting based on the user input and the machine output. Classifying also the results on the tree possible actions, rock, paper and scissors.

The machine is seeking for patterns.

For example: if the user decides to go for scissors more than a third of the time (not random probability), the machine will play rock more often than the other options.

The machines probability to play a certain option *grows/decreases* exponentially as the users actions repeat.


It also provides a historic record of results of matches if the user wants to know the info about the matches.

*And it can be played ad infinitum!*

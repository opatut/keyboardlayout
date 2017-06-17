# Keyboard Layout Optimizer

## The plan

1. record ourselves while typing all day, every day, for a long long time
    - this includes key strokes
    - and mouse movements
    - and their timings
2. find out a lot about what we're doing with the keyboard
    - n-grams of inputs
    - interpret selected modifier keys, don't interpret others
    - so we need all the data available
3. plot some fancy stats for maximum nerdiness
4. define a few metrics for penalty estimation of using keys in sequence
5. build an optimizer, e.g. genetic algorithm
    - maybe GPU optimize
    - modular penalty evaulation of sequences / n-grams
6. experiment with constraints
    - move/fix modifier keys
    - actually optimize special characters
    - why is the lowercase letter on the same key as the uppercase letter?
    - can we have special characters near the home row?
    - move around physical keys -> matrix design?

## Filtering / data extraction

* n-gram maximum duration / delay between keys
  - should be around 1-2 seconds per key I guess

## Penalties (things to consider)

* basic key penalty for distance from home position
* basic finger penalty for pinky/ring finger
* Same Hand Utilization (SHU)
* Same Finger Utilization (SFU)
* neighbor keys are sometimes good
* vertical movement vs horizontal movement
* actual hand base movement

### Basic ideas

* http://mkweb.bcgsc.ca/carpalx/?typing_effort
  - limited use of weak fingers, like pinky and ring finger
  - limited use of bottom row
  - increased use of home row
  - limited finger travel distance
  - limited same-finger typing (e.g. uhm)
  - balanced hand-use vs right-hand priority 
  - alternating hand-use vs rolling 

## More ideas

* is the finger/key mapping fixed?
* can we model keyboard shape dynamically (i.e. put key positions by keycode into the algorithm)

## Further reading

* http://mkweb.bcgsc.ca/carpalx/?
* https://gist.github.com/jonathanglasmeyer/5f44e10555726d121e0547d309e9d03a
* http://loup-vaillant.fr/articles/better-keyboards

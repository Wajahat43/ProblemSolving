Top down approach in this question doesn't work because we have to consider both current location and the currentFuel that we have it this location. This creates exponential possibilities. Since we could reach station i with multiple fuel levels.
​
Therefore, we need a bottom up approach for this question.
​
So If I am at station 5. We will check if we can reach this station from refueling at less than 5 fuel stations.
Assume we can reach station 5 with refueling at 2 stations before. Then we will say that the maximum distance we will reach by refueling at 3 stations would be max of prevous distance we could reach by 3 stations or by considering the 2stations from which we could reach currentstation + fuel at current station.
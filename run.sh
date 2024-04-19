# create a script to run 4 mappers with arguments, 4 reducers with arguments, and 1 master
# mapper and reducer with arguments
# run the script with the following command
# ./run.sh

#!/bin/bash

# Run 4 instances of Mapper.py
for i in 0 1 2 3; do
    python3 Mapper.py -i $i &
done

# Run 4 instances of Reducer.py
for i in 0 1 2 3; do
    python3 Reducer.py -i $i &
done

# Run 1 instance of Master.py
python3 Master.py

# Wait for all processes to finish
# now kill all the processes on the ports 50051 + 0/1/2/3
# also kill all the processes on the ports 50061 + 0/1/2/3

for i in {0..3}; do
    lsof -ti tcp:5005${i} | xargs kill -9
done

# Kill processes on ports 50061 + 0/1/2/3
for i in {0..3}; do
    lsof -ti tcp:5006${i} | xargs kill -9
done



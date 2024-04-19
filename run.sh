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

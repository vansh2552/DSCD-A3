import os
class Logger:
    def __init__(self, log_file, centroid_file, reducer_folder):
        self.log_file = log_file
        self.centroid_file = centroid_file
        self.reducer_folder = reducer_folder
        with open(self.log_file, 'w') as f:
            pass
        with open(self.centroid_file, 'w') as f:
            pass

        # create the reducer folder in the current directory
        curr_dir = os.getcwd()
        self.reducer_folder = os.path.join(curr_dir, self.reducer_folder)
        os.makedirs(self.reducer_folder, exist_ok=True)

        #
        # for file in os.listdir(self.reducer_folder):
        #     os.remove(os.path.join(self.reducer_folder, file))

    def log(self, message):
        print(message)
        
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')

    def log_centroids(self, centroids, iteration):
        # the centroid file is a txt file

        with open(self.centroid_file, 'a') as f:
            f.write(f"Iteration {iteration}\n")
            f.write(str(centroids) + '\n')

    def log_reducers(self, message, id):
        # in the reducer folder, create a file for each reducer
        # the file should be R{id+1}.txt
        # first create the txt file
        file_path = os.path.join(self.reducer_folder, f"R{id+1}.txt")
        with open(file_path, 'w') as f:
            f.write(message + '\n')

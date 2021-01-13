import time


class Runner:
    def __int__(self, algorithm):
        self.algorithm = algorithm

    def run_BFS(self):
        start_time = time.time()
        costs1 = self.algorithm.BFS()
        times = [time.time() - start_time]
        start_time = time.time()
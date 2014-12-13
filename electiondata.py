class ElectionResults:
  
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        self.file = open(self.filename, 'r')
        self.all_lines = self.file.readlines()

    def states(self):
        all_names = []
        for line in self.all_lines:
            columns = line.split(',')
            all_names.append(columns[1])
        return all_names[1:]

    def votes_count(self):
        total_votes = {'Obama': 0,
                       'Romney': 0}
        test = sum([int(line.split(',')[3]) for line in self.all_lines[1:]])
        print test
        total_votes['Obama'] = sum([int(line.split(',')[3]) for line in self.all_lines[1:]])
        total_votes['Romney'] = sum([int(line.split(',')[5]) for line in self.all_lines[1:]])
        return total_votes

    def state_count(self):
        return len(self.states())
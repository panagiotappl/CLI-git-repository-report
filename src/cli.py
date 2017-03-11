import git

repo = git.Repo("/home/feta/Desktop/Texnologia logismikou/CLI")
for commit in  repo.iter_commits():
    print commit.stats.total
print "Number of files: ", len(repo.index.entries)
# print repo.index.entries
print "Number of branches: ", len(repo.branches)
print "Number of tags: ", len(repo.tags)


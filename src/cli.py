import git

repo = git.Repo("/home/feta/Desktop/auction_site")
print len(repo.index.entries)
commit = list(repo.iter_commits()).pop()
print commit.stats.total
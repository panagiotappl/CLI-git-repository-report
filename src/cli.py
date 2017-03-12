from __future__ import division

import git
import sys


#get repository path from command line arguments
repo = git.Repo(sys.argv[1])

print "Number of files: ", len(repo.index.entries)
print "Number of branches: ", len(repo.branches)
print "Number of tags: ", len(repo.tags)

commits = list(repo.iter_commits())
print "Number of commits: ", len(commits)


authors = list()
commits_per_author = {}
for commit in commits:
    if commit.author not in authors:
        authors.append(commit.author)
        commits_per_author[commit.author] = 1
    else:
        commits_per_author[commit.author] += 1


print "Number of authors: ", len(authors)
print commits_per_author
print len(commits)

print "{:<25} {:<15}".format('Author','% of commits')
for author, comm in commits_per_author.iteritems():
    print "{:<25} {:<15}".format(author, str(comm/len(commits) * 100) + "%")
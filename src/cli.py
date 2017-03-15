import os
import sys
import re
import subprocess

def number_of_files():
    command = "git ls-files"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    rows = process.readlines()
    process.close()

    return len(rows)

def number_of_lines():
    command = "git ls-files | xargs wc -l"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    rows = process.readlines()

    return rows[len(rows) - 1].strip().split(' ', 1)[0]

def committer_stats():
    # Number of committers
    command = "git log --all --format='%aN' | sort -u "
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    rows = process.readlines()
    process.close()

    commiters = []
    for j in range(0, len(rows)):
        commiters.append(rows[j].decode("utf-8", "replace").strip())
    print "Number of committers: ", len(commiters)

    # Number of commits
    command = "git shortlog --all | grep -E '^[ ]+\w+' | wc -l"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    rows = process.readlines()
    process.close()

    commits = rows[0]
    print "Number of commits: ", commits
    print

    # Number of insertions/deletions per committer
    print "Number of insertions/deletions per committer:"
    for i in range(0, len(commiters)):
        command = 'git log --all --author="' + commiters[i] + '" --oneline --shortstat'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout

        adds, dels = 0, 0
        for line in process.readlines():
            am, dm = re.search(r'\d+(?= insertions)', line), re.search(r'\d+(?= deletions)', line)
            if am is not None:
                adds += int(am.group())
            if dm is not None:
                dels += int(dm.group())
        process.close()

        print commiters[i], ": ", adds, " insertions (+), ",  dels, " deletions(-)"
    print

    # Number of commits per author
    command = "git shortlog -sn --all"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout

    rows = process.readlines()
    process.close()

    commits_per_author = {}
    print "Number of commits per author: "
    for i in range(0, len(rows)):
        commits_per_author[rows[i].strip().split('\t', 1)[1]] = rows[i].strip().split('\t', 1)[0]


    for i in commits_per_author:
        percentage = float(commits_per_author[i])/float(commits) * 100
        print i, ": ", round(percentage, 2), "%"

def main():
    repo_path = sys.argv[1]
    os.chdir(repo_path)

    file_count = number_of_files()
    print "Number of files: ", file_count

    line_count_total = number_of_lines()
    print "Total number of lines: ", line_count_total

    committer_stats()
    print

if __name__ == "__main__":
	main()
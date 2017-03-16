import os
import sys
import re
import subprocess


def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    result = process.readlines()
    process.close()

    return result


def number_of_files():
    results = execute_command("git ls-files")
    return len(results)


def number_of_lines():
    results = execute_command("git ls-files | xargs wc -l")
    return results[len(results) - 1].strip().split(' ', 1)[0]


def committer_stats():
    # Number of committers
    results = execute_command("git log --all --format='%aN' | sort -u")

    commiters = []
    for j in range(0, len(results)):
        commiters.append(results[j].decode("utf-8", "replace").strip())
    print "Number of committers: ", len(commiters)

    # Number of commits
    results = execute_command("git shortlog --all | grep -E '^[ ]+\w+' | wc -l")

    commits = results[0]
    print "Number of commits: ", commits
    print

    # Number of insertions/deletions per committer
    print "Number of insertions/deletions per committer:"
    for j in range(0, len(commiters)):
        results = execute_command('git log --all --author="' + commiters[j] + '" --oneline --shortstat')

        adds, dels = 0, 0
        for i in range(0, len(results)):
            am, dm = re.search(r'\d+(?= insertions)', results[i]), re.search(r'\d+(?= deletions)', results[i])
            if am is not None:
                adds += int(am.group())
            if dm is not None:
                dels += int(dm.group())

        print commiters[j], ": ", adds, " insertions (+), ", dels, " deletions(-)"
    print

    # Number of commits per author
    results = execute_command("git shortlog -sn --all")

    commits_per_author = {}
    print "Percentage of commits per author: "
    for i in range(0, len(results)):
        commits_per_author[results[i].strip().split('\t', 1)[1]] = results[i].strip().split('\t', 1)[0]

    for i in commits_per_author:
        percentage = float(commits_per_author[i]) / float(commits) * 100
        print i, ": ", round(percentage, 2), "%"

def branch_stats():
    # Number of branches (local)
    localB = execute_command("git branch")
    print "Number of branches (local): ", len(localB)


    # Number of branches (remote)
    remoteB = execute_command("git branch -r")
    print "Number of branches (remote): ", len(remoteB) - 1
    print

    # Number of commits per branch (remote)
    print "Number of commits per branch: "
    for i in range(1, len(remoteB)):
        result = execute_command("git rev-list --count" + remoteB[i])
        print remoteB[i].strip(), ": ", int(result[0])
    print

def main():
    repo_path = sys.argv[1]
    os.chdir(repo_path)

    file_count = number_of_files()
    print "Number of files: ", file_count

    line_count_total = number_of_lines()
    print "Total number of lines: ", line_count_total

    committer_stats()
    print

    branch_stats()


if __name__ == "__main__":
    main()

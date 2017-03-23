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
    """
    Returns lines count.

    :return: returns number of lines of git-included files
    """
    # xargs to uild and execute wc from standard input.
    results = execute_command("git ls-files | xargs wc -l")
    return results[len(results) - 1].strip().split(' ', 1)[0]


def committer_stats():
    """
    Generates and prints commiter's stats.
    """
    results = execute_command("git log --all --format='%aN' | sort -u")

    commiters = []
    for j in range(0, len(results)):
        commiters.append(results[j].decode("utf-8", "replace").strip())
    print "Number of committers: ", len(commiters)

    # Number of commits
    result = execute_command("git shortlog --all | grep -E '^[ ]+\w+' | wc -l")

    commits = result[0]
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

    # Percentage of commits per author.
    results = execute_command("git shortlog -sn --all")

    commits_per_author = {}
    print "Percentage of commits per author: "
    for i in range(0, len(results)):
        commits_per_author[results[i].strip().split('\t', 1)[1]] = results[i].strip().split('\t', 1)[0]

    for i in commits_per_author:
        percentage = float(commits_per_author[i]) / float(commits) * 100
        # Print readable percentage per author.
        print i, ": ", round(percentage, 2), "%"

def branch_stats():
    """
    Generates and prints branches stats.
    """
    # Number of branches (local).
    localB = execute_command("git branch")
    print "Number of branches (local): ", len(localB)


    # Number of branches (remote).
    remoteB = execute_command("git branch -r")
    print "Number of branches (remote): ", len(remoteB) - 1
    print

    # Number of commits per branch (remote).
    print "Number of commits per remote branch: "
    # Ignore first element (HEAD pointer).
    for i in range(1, len(remoteB)):
        result = execute_command("git rev-list --count" + remoteB[i])
        print remoteB[i].strip(), ": ", int(result[0])
    print

    # Number of commits per branch (local)
    print "Number of commits per local branch: "
    for i in range(0, len(localB)):
        # Remove star character for edited local branches
        result = execute_command("git rev-list --count " + localB[i].strip('* '))
        print localB[i].strip(), ": ", int(result[0])
    print


    # Commit percentage per branch per author (remote)
    # Ignore first element (HEAD pointer).
    print "Commits per remote branch per author:\n"
    for branch in remoteB[1:]:
        branch_total_commits = execute_command("git rev-list --count " + branch)[0].strip()
        result = execute_command("git shortlog -sn " + branch)
        print branch.strip() + ": "
        for res in result:
            commits = res.strip()[0]
            name = res.strip()[1:].strip()
            percentage = float(commits) / float(branch_total_commits) * 100
            print "\t\t" + name + ": %10.2f" % round(percentage, 2) + "%"
    print


    # Commit percentage per branch per author (local)
    # Ignore first element (HEAD pointer).
    print "Commits per local branch per author:\n"
    for branch in localB:
        branch = branch.strip('* ')
        branch_total_commits = execute_command("git rev-list --count " + branch)[0].strip()
        result = execute_command("git shortlog -sn " + branch)
        print branch.strip() + ": "
        for res in result:
            commits = res.strip()[0]
            name = res.strip()[1:].strip()
            percentage = float(commits) / float(branch_total_commits) * 100
            print "\t\t" + name + ": %10.2f" % round(percentage, 2) + "%"



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

import os
import sys
import re
import subprocess

from datetime import datetime


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
    print


    # Get mean commit's rate per day, week and month
    print "Commit rates per day, week and month: "
    print
    # Find earliest commit.
    earliest_commit = execute_command("git rev-list --max-parents=0 HEAD")
    earliest_commit = execute_command("git show -s --format=%ci " + earliest_commit[0].strip())[0].strip()

    # Calculate days since then.
    date_format = "%Y-%m-%d"
    first_commit_date = datetime.strptime(earliest_commit.split(" ")[0], date_format)
    today = datetime.now()

    days = today - first_commit_date
    days = days.days

    results = execute_command("git shortlog -sn --all")

    for res in results:
        res = res.strip()
        commits = res[0]
        res = res[1:]
        name = res.strip()
        print name + " " + str(round(float(commits)/float(days), 3)) + " commits per day."
        # A week is 7 days.
        print name + " " + str(round(float(commits) / float(days) * 7, 3)) + " commits per week."
        # A month is 30.
        print name + " " + str(round(float(commits) / float(days) * 30, 3)) + " commits per month."
        print
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

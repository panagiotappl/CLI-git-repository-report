import os
import sys
import re
import subprocess
from datetime import datetime
from output import generate_output
from itertools import izip

def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout
    result = process.readlines()
    process.close()

    return result


def grouped(iterable, n):
    "s -> (s0,s1,s2,...sn-1), (sn,sn+1,sn+2,...s2n-1), (s2n,s2n+1,s2n+2,...s3n-1), ..."
    return izip(*[iter(iterable)]*n)


def repo_name():
    results = execute_command("git rev-parse --show-toplevel")
    return results[0]


def number_of_files():
    results = execute_command("git ls-files")
    return len(results)


def number_of_lines():
    """
    Returns lines count.

    :return: returns number of lines of git-included files
    """
    # xargs to uild and execute wc from standard input.
    results = execute_command("git diff --stat 4b825dc642cb6eb9a060e54bf8d69288fbee4904")
    lines = 0
    for file in results:
        t = int(re.findall(" /|\s+(\d+)\s+", file)[0])
        lines += t
    return lines


def committer_stats():
    """
    Generates and prints commiter's stats.
    """
    com_stats = dict()
    results = execute_command("git log --all --format='%aN'")
    results = map(str.strip, results)
    results.sort()
    results = set(results)

    commiters = []
    for commiter in results:
        commiters.append(commiter.decode("utf-8", "replace").strip())
    print "Number of committers: ", len(commiters)

    com_stats["committers"] = len(commiters)
    # Number of commits
    # result = execute_command("git shortlog --all | grep -E '^[ ]+\w+' | wc -l")
    result = execute_command(" git shortlog --all -s")
    commits = 0
    for author in result:
        commits += int(re.findall("\s(\d+)\t", author)[0])

    com_stats["commits"] = commits
    print "Number of commits: ", commits
    print

    com_adds = dict()
    com_dels = dict()
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
        com_adds[commiters[j]] = adds
        com_dels[commiters[j]] = dels
        print commiters[j], ": ", adds, " insertions (+), ", dels, " deletions(-)"
    print
    com_stats["adds"] = com_adds
    com_stats["dels"] = com_dels

    # Percentage of commits per author.
    results = execute_command("git shortlog -sn --all")

    commits_per_author = dict()
    print "Percentage of commits per author: "
    for i in range(0, len(results)):
        commits_per_author[results[i].strip().split('\t', 1)[1]] = results[i].strip().split('\t', 1)[0]

    for author in commits_per_author:
        commits_per_author[author] =  round(float(commits_per_author[author]) / float(commits) * 100, 2)

    com_stats["com_per_author"] = commits_per_author
    for i in commits_per_author:
        percentage = float(commits_per_author[i]) / float(commits) * 100
        # Print readable percentage per author.
        print i, ": ", round(percentage, 2), "%"

    return com_stats


def branch_stats():
    """
    Generates and prints branches stats.
    """

    br_stats = dict()

    # Number of tags
    tags = execute_command("git tag")
    br_stats["tags"] = len(tags)
    # Number of branches (local).
    localB = execute_command("git branch")
    print "Number of branches (local): ", len(localB)

    # Number of branches (remote).
    remoteB = execute_command("git branch -r")
    print "Number of branches (remote): ", len(remoteB) - 1
    print

    br_stats["localCount"] = len(localB)
    br_stats["remoteCount"] = len(remoteB)
    br_stats["localB"] = localB
    br_stats["remoteB"] = remoteB[1:]
    br_stats['branch_dates_remote'] = {}
    br_stats['branch_dates_local'] = {}
    br_stats['branch_stats_local'] = {}
    br_stats['branch_stats_remote'] = {}

    com_branchR = dict()
    # Number of commits per branch (remote).
    print "Number of commits per remote branch: "
    # Ignore first element (HEAD pointer).
    for i in range(1, len(remoteB)):
        result = execute_command("git rev-list --count" + remoteB[i])
        com_branchR[remoteB[i].strip()] = int(result[0])
        print remoteB[i].strip(), ": ", int(result[0])
        # Also get branch dates
        res = execute_command("git reflog --pretty='%cd' " + remoteB[i])
        if res:
            br_stats['branch_dates_remote'][remoteB[i].strip()] = [res[-1] , res[0]]
        else:
            br_stats['branch_dates_remote'][remoteB[i].strip()] = [0,0]
        # Also get branches logs
        res = execute_command('git log ' + remoteB[i].strip() + ' --pretty="tformat:\"%h@@@%ad@@@%s%d@@@%an\"" --date=short')
        br_stats['branch_stats_remote'][remoteB[i].strip()] = []
        for commit in res:
            commit = commit[1:].strip()
            data = commit.split("@@@")
            br_stats['branch_stats_remote'][remoteB[i].strip()].append(
                {
                    'id': data[0],
                    'message': data[2],
                    'date': data[1],
                    'author': data[3].strip()

                }
            )
    print

    br_stats["tagsR"] = {}

    for branch in remoteB[1:]:
        br_stats["tagsR"][branch.strip] = []



    br_stats["com_branchR"] = com_branchR

    com_branchL = dict()
    # Number of commits per branch (local)
    print "Number of commits per local branch: "
    for i in range(0, len(localB)):
        # Remove star character for edited local branches
        result = execute_command("git rev-list --count " + localB[i].strip('* '))
        com_branchL[localB[i].strip()] = int(result[0])
        print localB[i].strip(), ": ", int(result[0])
        # Also get branch dates
        res = execute_command("git reflog --pretty='%cd' " + localB[i].strip('* '))
        if res:
            br_stats['branch_dates_local'][localB[i].strip('* \n')] = [res[-1] , res[0]]
        else:
            br_stats['branch_dates_local'][localB[i].strip('* \n')] = [0, 0]
        # Also get branches logs
        res = execute_command('git log ' + localB[i].strip('* \n') + ' --pretty="tformat:\"%h@@@%ad@@@%s%d@@@%an\"" --date=short')
        br_stats['branch_stats_local'][localB[i].strip('* \n')] = []
        for commit in res:
            commit = commit[1:].strip()
            data = commit.split("@@@")
            br_stats['branch_stats_local'][localB[i].strip('* \n')].append(
                {
                    'id': data[0],
                    'message': data[2],
                    'date': data[1],
                    'author': data[3].strip()

                }
            )
    print


    for branch in localB:
        br_stats["tagsR"][branch.strip()] = []
    tags = execute_command("git tags")
    for tag in tags:
        res = execute_command("git branch --contains tags/"+tag.strip())
        for branch in res:
            br_stats["tagsR"][branch.strip()].append(tag.strip())

    br_stats["com_branchL"] = com_branchL

    com_br_authR = dict()
    # Commit percentage per branch per author (remote)
    # Ignore first element (HEAD pointer).
    print "Commits per remote branch per author:\n"
    for branch in remoteB[1:]:
        branch_total_commits = execute_command("git rev-list --count " + branch)[0].strip()
        result = execute_command("git shortlog -sn " + branch)
        print branch.strip() + ": "
        com_br_authR[branch.strip()] = []
        for res in result:
            commits = res.split()[0]
            name = res.split()[1]
            percentage = float(commits) / float(branch_total_commits) * 100
            com_br_authR[branch.strip()].append([name, percentage])
            print "\t\t" + name + ": %10.2f" % round(percentage, 2) + "%"
    print

    br_stats["com_br_authR"] = com_br_authR

    com_br_authL = dict()
    # Commit percentage per branch per author (local)
    # Ignore first element (HEAD pointer).
    print "Commits per local branch per author:\n"
    for branch in localB:
        branch = branch.strip('* ')
        branch_total_commits = execute_command("git rev-list --count " + branch)[0].strip()
        result = execute_command("git shortlog -sn " + branch)
        print branch.strip() + ": "
        com_br_authL[branch.strip()] = []
        for res in result:
            commits = res.split()[0]
            name = res.split()[1]
            percentage = float(commits) / float(branch_total_commits) * 100
            com_br_authL[branch.strip()].append([name, percentage])
            print "\t\t" + name + ": %10.2f" % round(percentage, 2) + "%"
    print

    br_stats["com_br_authL"] = com_br_authL

    com_rates = dict()
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
        res = res.split('\t')
        commits = res[0]
        name = res[1]
        com_rates[name] = [round(float(commits) / float(days), 3), round(float(commits) / float(days) * 7, 3),
                           round(float(commits) / float(days) * 30, 3)]
        print name + " " + str(round(float(commits) / float(days), 3)) + " commits per day."
        # A week is 7 days.
        print name + " " + str(round(float(commits) / float(days) * 7, 3)) + " commits per week."
        # A month is 30.
        print name + " " + str(round(float(commits) / float(days) * 30, 3)) + " commits per month."
        print
    print

    br_stats["com_rates"] = com_rates

    return br_stats


def main():
    repo_path = sys.argv[1]
    output_path = sys.argv[2]

    os.chdir(repo_path)

    statistics = dict()

    statistics["gitname"] = repo_name()

    statistics["file_count"] = number_of_files()

    statistics["line_count_total"] = number_of_lines()

    statistics["com_stats"] = committer_stats()

    statistics["br_stats"] = branch_stats()

    generate_output(statistics, output_path)
    print statistics


if __name__ == "__main__":
    main()

import os
import sys
import plotly
import re
import subprocess
from datetime import datetime
from output import generate_output
from itertools import izip

def execute_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout
    result = process.readlines()
    process.close()
    a = plotly.colors
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

    com_stats["committers"] = len(commiters)
    # Number of commits
    # result = execute_command("git shortlog --all | grep -E '^[ ]+\w+' | wc -l")
    result = execute_command(" git shortlog --all -s")
    commits = 0
    for author in result:
        commits += int(re.findall("\s(\d+)\t", author)[0])

    com_stats["commits"] = commits

    com_adds = {}
    com_dels = {}
    com_changes = {}
    # Number of insertions/deletions per committer
    for j in range(0, len(commiters)):
        results = execute_command('git log --all --author="' + commiters[j] + '" --oneline --shortstat')
        lines_added = 0
        lines_moddified = 0
        lines_removed = 0
        for res in results:
            am, dm = re.search(r'\d+(?= insertions)', res), re.search(r'\d+(?= deletions)', res)
            MOD_PATTERN = '^.+(\[-|\{\+).*$'
            ADD_PATTERN = '^\{\+.*\+\}$'
            REM_PATTERN = '^\[-.*-\]$'


            if not (am and dm):
                commit = res.split(' ')[0]
            if am or dm:
                dif = execute_command("git diff --word-diff --unified=0 " + commit + " " + commit + "~1")
                for line in dif:
                    addsMatch = re.findall(ADD_PATTERN, line)
                    changesMatch = re.findall(MOD_PATTERN, line)
                    removedMatch = re.findall(REM_PATTERN, line)
                    if addsMatch:
                        lines_added += 1
                    if changesMatch:
                        lines_moddified += 1
                    if removedMatch:
                        lines_removed += 1

        com_adds[commiters[j]] = lines_added
        com_dels[commiters[j]] = lines_removed
        com_changes[commiters[j]] = lines_moddified
    com_stats["adds"] = com_adds
    com_stats["dels"] = com_dels
    com_stats["changes"] = com_changes

    # Percentage of commits per author.
    results = execute_command("git shortlog -sn --all")

    commits_per_author = dict()
    for i in range(0, len(results)):
        commits_per_author[results[i].strip().split('\t', 1)[1]] = results[i].strip().split('\t', 1)[0]

    for author in commits_per_author:
        commits_per_author[author] = round(float(commits_per_author[author]) / float(commits) * 100, 2)

    com_stats["com_per_author"] = commits_per_author
    for i in commits_per_author:
        percentage = float(commits_per_author[i]) / float(commits) * 100
        # Print readable percentage per author.

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

    # Number of branches (remote).
    remoteB = execute_command("git branch -r")

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
    # Ignore first element (HEAD pointer).
    for i in range(1, len(remoteB)):
        result = execute_command("git rev-list --count" + remoteB[i])
        com_branchR[remoteB[i].strip()] = int(result[0])
        # Also get branch dates
        res = execute_command("git log --pretty='%cd' " + remoteB[i])
        first = execute_command("git show-branch --sha1 master " + remoteB[i])
        first_commit = first[-1]
        first_sha1 = re.findall(r'\[([^]]*)\]', first_commit)[0]
        date = execute_command("git show -s --format=%ci "+ first_sha1)[0]
        if res:
            if len(first) is 1:
                date = res[-1]
            br_stats['branch_dates_remote'][remoteB[i].strip()] = [date , res[0]]
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

    br_stats["tagsR"] = {}

    for branch in remoteB[1:]:
        br_stats["tagsR"][branch.strip] = []



    br_stats["com_branchR"] = com_branchR

    com_branchL = dict()
    # Number of commits per branch (local)
    for i in range(0, len(localB)):
        # Remove star character for edited local branches
        result = execute_command("git rev-list --count " + localB[i].strip('* '))
        com_branchL[localB[i].strip()] = int(result[0])
        # Also get branch dates
        res = execute_command("git log --pretty='%cd' " + localB[i].strip('* '))
        first = execute_command("git show-branch --sha1 master " + localB[i].strip('* '))
        first_commit = first[-1]
        first_sha1 = re.findall(r'\[([^]]*)\]', first_commit)[0]
        date = execute_command("git show -s --format=%ci "+ first_sha1)[0]
        if res:
            if len(first) is 1:
                date = res[-1]
            br_stats['branch_dates_local'][localB[i].strip('* \n')] = [date , res[0]]
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


    for branch in localB:
        br_stats["tagsR"][branch.strip()] = []
    tags = execute_command("git tag")
    for tag in tags:
        res = execute_command("git branch --contains tags/"+tag.strip())
        for branch in res:
            br_stats["tagsR"][branch.strip()].append(tag.strip())

    br_stats["com_branchL"] = com_branchL

    com_br_authR = dict()
    # Commit percentage per branch per author (remote)
    # Ignore first element (HEAD pointer).
    for branch in remoteB[1:]:
        branch_total_commits = execute_command("git rev-list --count " + branch)[0].strip()
        result = execute_command("git shortlog -sn " + branch)
        com_br_authR[branch.strip()] = []
        for res in result:
            commits = res.split()[0]
            name = res.split()[1]
            percentage = round(float(commits) / float(branch_total_commits) * 100, 2)
            com_br_authR[branch.strip()].append([name, percentage])

    br_stats["com_br_authR"] = com_br_authR

    com_br_authL = dict()
    # Commit percentage per branch per author (local)
    # Ignore first element (HEAD pointer).
    for branch in localB:
        branch = branch.strip('* ')
        branch_total_commits = execute_command("git rev-list --count " + branch)[0].strip()
        result = execute_command("git shortlog -sn " + branch)
        com_br_authL[branch.strip()] = []
        for res in result:
            commits = res.split()[0]
            name = res.split()[1]
            percentage = round(float(commits) / float(branch_total_commits) * 100, 2)
            com_br_authL[branch.strip()].append([name, percentage])

    br_stats["com_br_authL"] = com_br_authL

    com_rates = dict()
    # Get mean commit's rate per day, week and month
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
        # A week is 7 days.
        # A month is 30.

    br_stats["com_rates"] = com_rates

    return br_stats



def analyze():

    statistics = dict()

    statistics["gitname"] = repo_name()

    statistics["file_count"] = number_of_files()

    statistics["line_count_total"] = number_of_lines()

    statistics["com_stats"] = committer_stats()

    statistics["br_stats"] = branch_stats()

    return statistics


def check_validation():
    result = execute_command("git rev-parse --is-inside-work-tree")
    if len(result) == 0 or result[0].strip('\n') != "true":
        print "Not a valid git repository."
        sys.exit()


def main():
    if len(sys.argv) < 3:
        print "Missing arguments."
        print "Usage: java -jar cli.jar <git_repo_path> <html_output_path>"
        return

    repo_path = sys.argv[1]
    output_path = sys.argv[2]

    os.chdir(repo_path)

    check_validation()

    statistics = analyze()

    generate_output(statistics, output_path)
    #print statistics

if __name__ == "__main__":
    main()

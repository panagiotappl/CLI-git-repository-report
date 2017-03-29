The whole project has been developed in Python 2.7 with the use of d3pie for a cool pie for committers percentages.

The stats extraction is done through CLI git commands and python data manipulation techniques.

There is also implemented a stats extraction for remote branches but it was commented out due
to the realisation that it wasn't a part of the requirements.

We used the jython standalone jar to run the programm in JVM since this was a requirement.

Specificaly for each statistic:

* Number of files.
    + By getting the length of `git ls-files` results.

* Number of tracked files lines.
    + Using `git diff --stat 4b825dc642cb6eb9a060e54bf8d69288fbee4904` which shows the differences from the empty tree to the current working tree. This is also
    returning the number of lines of each tracked file.

* Number of branches.
    + By counting the length of `git branch` command.

* Number of tags.
    + By counting the length of `git tag` command.

* Number of authors.
    + By using `git log --all --format='%aN'` to filter only the authors names (`--format='%aN'`) from commits all across the repo (`-all`)
    and counting the unique strings of the results.

* Branch statistics table with dates.
    + By iterating over `git branch` results to run commands for each branch.
    + We are getting number of commits per branch using the `git rev-list --count <branch_name>` command.
    + We calculate the creating and modification dates by using `git log --pretty='%cd'  <branch_name>` to find the date of the last commit
      and git `git show-branch --sha1 master <branch_name>` to identify in which commit <branch_name> is diverting from master. This is the point that the branch was created.

* Commits of each branch.
    + By using `git rev-list --count <branch_name>` to get number of commits on <branch_name> .

* Tags of each branch.
    * Tags are not branch-specific but we can indetify if the commit a tag points to is part of the branch.
    * This is done by using `git tag` to get all the tags of the repo and then for each tag `git branch --contains tags/<tag_name>` to identify in which branches the tag appears.

* Number of commits.
    + By using the `git shortlog --all -s` command to get commits count from all branches.

* Commits percentage per author.
    + By using the `git shortlog --all -s` command to get commits/author from all branches.

* Commits percentage per branch.
    + By using `git rev-list --remotes` to get all the commits across all branches. Then this is used to calculate percentages per branch.
      We can identify number of commits per branch using the `git log --pretty=format:"%h" <branch_name>` command.
* Commits percentage per branch per author.
    + By using `git shortlog -sn <branch_name>` to get number of commits per author per branch (by iterating over the branches).

* Average commits per day, week, month per author.
    + By calculating the time-span of the project on days and then getting the average commits per user per day (users_commits/days).
     Then this is multiplied by 7 to get weeks average and by 30 to get months average

* Average number of lines added, edited, removed  per author.
    + By using the following regular expressions to filter the results of `"git diff --word-diff --unified=0 <commit_name> <commit_name>~1"` which diffs a commit with it's previeous.
    ```
            MOD_PATTERN = '^.+(\[-|\{\+).*$'
            ADD_PATTERN = '^\{\+.*\+\}$'
            REM_PATTERN = '^\[-.*-\]$'
     ```
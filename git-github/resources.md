1. Git Internals
The Git object model: blobs, trees, commits, and tags

How Git stores references (branches, tags)

The Git directory structure (.git folder contents)

The Git index (staging area) mechanics

Git's directed acyclic graph (DAG) of commits

2. Advanced Branching Strategies
Git flow workflow

GitHub flow

Trunk-based development

Long-running branches vs. feature flags

Branch naming conventions and strategies

3. Advanced Merging and Rebasing
Recursive merge strategy

Octopus merges

Resolving complex merge conflicts

Interactive rebasing with squash, fixup, etc.

When to merge vs. when to rebase

Rebase --onto for complex branch restructuring

4. Advanced Stashing
Stash with message

Stash specific files

Creating branches from stashes

Stash apply vs. pop

Stash with untracked files

5. Advanced Log and History
Custom formatting with --pretty

Searching history with -S and -G

Filtering commits by path, author, date, etc.

Using git bisect for bug hunting

Reflog usage and recovery

6. Hooks and Automation
Pre-commit, pre-push hooks

Server-side hooks

Custom Git commands

Git aliases for complex operations

Integrating with CI/CD pipelines

7. Submodules and Subtrees
When to use each

Managing dependencies

Updating submodules

Converting between submodules and subtrees

Handling nested submodules

8. Advanced Remote Operations
Multiple remotes management

Remote tracking branches

Push strategies (simple, matching)

Fetching specific branches

Pruning stale references

9. Performance Optimization
Shallow clones

Partial clones

Sparse checkouts

Git garbage collection

Packfiles and compression

10. Security Considerations
Signed commits and tags

GPG integration

Managing sensitive data

Audit trails

Repository permissions

100 Intermediate to Advanced Git Interview Questions


Intermediate Questions (1-40)

Explain the difference between git fetch and git pull.
- git fetch downloads remote changes without merging; git pull does fetch + merge.

How do you squash multiple commits into one?


What is the difference between git merge and git rebase?

How would you resolve a merge conflict?

Explain what git stash does and when you might use it.

What is the purpose of .gitignore file?

How do you rename a Git branch locally and remotely?

What is the difference between HEAD, working tree, and index?

How do you discard local changes in a file?

What is a detached HEAD state and how do you fix it?

How do you view the changes made in a specific commit?

What is the difference between git reset --soft, --mixed, and --hard?

How do you create and apply a Git patch?

What is git cherry-pick and when would you use it?

How do you find which commit introduced a bug?

What are Git hooks and how would you use them?

How do you change the message of the last commit?

What is the purpose of git reflog?

How do you delete a branch locally and remotely?

What is the difference between git rm and git reset for removing files?

How do you compare two branches?

What is a fast-forward merge and how is it different from a three-way merge?

How do you list all remote branches?

What is the purpose of git blame?

How do you revert a specific file to a previous version?

What is the difference between git pull --rebase and regular git pull?

How do you set up Git to ignore changes in file permissions?

What is the purpose of git clean?

How do you find all commits that contain a specific string?

What is the difference between origin/master and master?

How do you change the URL of a remote repository?

What is the purpose of git tag and how do you create one?

How do you push tags to a remote repository?

What is git bisect and how does it work?

How do you list all aliases in Git?

What is the purpose of git archive?

How do you create and apply a Git patch?

What is the difference between git diff and git difftool?

How do you configure Git to use a specific editor for commit messages?

What is the purpose of git submodule and how do you use it?

Advanced Questions (41-80)
Explain Git's object model and how it stores data.

What are the advantages of using a rebase workflow vs. a merge workflow?

How would you rewrite history to remove a large file accidentally committed?

Explain how Git stores branches internally.

What is the difference between git rebase -i and git filter-branch?

How would you handle a situation where you need to maintain a fork that diverges significantly from upstream?

What is the purpose of git worktree and when would you use it?

How do you convert a Git repository to use shallow clone?

Explain how Git's packfiles work.

What is the purpose of git replace and when would you use it?

How would you implement a CI/CD pipeline that only runs tests on changed files?

What are Git's garbage collection mechanisms and how do they work?

How would you optimize a repository with a very large history?

Explain how Git's delta compression works.

What is the purpose of git notes and how would you use it?

How would you implement a deployment strategy using Git hooks?

What are Git's transfer protocols and how do they differ?

How would you handle binary files in a Git repository?

What is Git LFS and when would you use it?

How would you implement a code review workflow using Git?

What are Git's strategies for handling line endings across platforms?

How would you implement a hook to prevent commits that don't meet certain criteria?

What is the purpose of git bundle and when would you use it?

How would you recover a deleted branch that doesn't appear in git reflog?

What are Git's mechanisms for handling large repositories?

How would you implement a custom merge strategy?

What is the purpose of git credential helpers?

How would you implement a deployment strategy using Git tags?

What are Git's mechanisms for signing commits and tags?

How would you handle a situation where you need to maintain configuration files that differ between environments?

What is the purpose of git filter-repo and how does it differ from filter-branch?

How would you implement a Git-based backup system?

What are Git's mechanisms for handling submodules in large projects?

How would you implement a Git-based documentation system?

What are Git's mechanisms for handling authentication in enterprise environments?

How would you implement a Git-based configuration management system?

What are Git's mechanisms for handling merge conflicts in binary files?

How would you implement a Git-based content management system?

What are Git's mechanisms for handling repository corruption?

How would you implement a Git-based artifact repository?

Expert-Level Questions (81-100)
Explain how you would design a distributed version control system like Git from scratch.

How would you scale Git to handle millions of repositories in an enterprise environment?

What are the performance characteristics of Git's object database under heavy load?

How would you implement a Git server with custom authentication and authorization?

What are the security considerations when hosting Git repositories?

How would you implement a Git proxy server to cache repositories?

What are the challenges of implementing Git on top of a distributed filesystem?

How would you design a Git hosting service with high availability?

What are the performance implications of Git's garbage collection on large repositories?

How would you implement a Git-based system for managing infrastructure as code?

What are the challenges of implementing Git for very large binary assets?

How would you design a Git workflow for a globally distributed team?

What are the implications of Git's design for repository size and performance?

How would you implement a Git-based system for managing machine learning models?

What are the challenges of implementing Git for databases?

How would you design a Git-based system for managing configuration across microservices?

What are the performance characteristics of Git's network protocols under high latency?

How would you implement a Git-based system for managing secrets?

What are the challenges of implementing Git for very large monorepos?

How would you design a Git-based system for managing documentation across multiple products?


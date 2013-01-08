#! /usr/bin/env python
#
# Copyright: John C Barstow 2013
# License: GPLv2+
#
'''branching

Manage feature branches.
'''

from mercurial import commands, hg

def harvest(ui, repo, branch, **opts):
    """Merge a branch into default"""
    if branch not in repo.branchtags():
        ui.warn("Branch %s does not exist! (use 'hg branches' to get a list of branches)\n" % branch)
        return

    #todo: verify branch is open and has one head
    hg.clean(repo, branch)
    repo.commit("Closed branch %s" % branch, opts.get('user'), opts.get('date'), None, extra={'close':1})
    hg.clean(repo, "default")
    hg.merge(repo, branch)
    repo.commit("Merged %s" % branch, opts.get('user'), opts.get('date'), None)
    ui.status("Completed merge of %s\n" % branch)

def close_branch(ui, repo, branch, **opts):
    """Close a branch"""
    if branch not in repo.branchtags():
        ui.warn("Branch %s does not exist! (use 'hg branches' to get a list of branches)\n" % branch)
        return

    #todo: verify branch is open and has one head
    hg.clean(repo, branch)
    repo.commit("Closed branch %s" % branch, opts.get('user'), opts.get('date'), None, extra={'close':1})
    hg.clean(repo, "default")

def switch_branch(ui, repo, branch, **opts):
    """Switch to the named branch"""
    if branch not in repo.branchtags():
        ui.warn("Branch %s does not exist! (use 'hg branches' to get a list of branches)\n" % branch)
        return
    hg.clean(repo, branch)

cmdtable = {
        "harvest": (harvest, [], "hg harvest BRANCH_NAME"),
        "close": (close_branch, [], "hg close BRANCH_NAME"),
        "switch": (switch_branch, [], "hg switch BRANCH_NAME"),
}


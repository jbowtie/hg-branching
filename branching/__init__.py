#! /usr/bin/env python
#
# Copyright: John C Barstow 2013
# License: GPLv2+
#
'''commands to manage named branches'''

from mercurial import commands, hg, context

def harvest(ui, repo, branch, dest="default", **opts):
    """Close and merge a named branch into the destination branch"""
    if branch not in repo.branchtags():
        ui.warn("Branch %s does not exist! (use 'hg branches' to get a list of branches)\n" % branch)
        return

    if dest not in repo.branchtags():
        ui.warn("Destination branch %s does not exist! (use 'hg branches' to get a list of branches)\n" % branch)
        return

    heads = repo.branchheads(branch)
    if len(heads) == 0:
        ui.warn("Cannot harvest branch %s because it is currently closed. \nUse 'hg merge' to merge it manually.\n" % branch)
        return

    if len(heads) > 1:
        ui.warn("Branch %s has multiple heads. \nUse 'hg merge' to merge it manually.\n" % branch)
        return

    rev = repo.branchtip(branch)
    newrev = context.memctx(repo, [rev, None], "Closed branch %s" % branch, [], None, opts.get('user'), opts.get('date'), extra={'close':1, 'branch':branch})
    newrev.commit()

    #don't need to switch if already on destination branch
    curr = repo[None].branch()
    if dest != curr:
        hg.clean(repo, dest)
        ui.status("Switched to branch %s before merging\n" % dest)

    hg.merge(repo, branch)
    repo.commit("Merged %s" % branch, opts.get('user'), opts.get('date'), None)
    ui.status("Completed merge of %s into %s\n" % (branch, dest))

def close_branch(ui, repo, branch, **opts):
    """Close a branch"""
    if branch not in repo.branchtags():
        ui.warn("Branch %s does not exist! (use 'hg branches' to get a list of branches)\n" % branch)
        return

    heads = repo.branchheads(branch)
    if len(heads) == 0:
        ui.status("Branch %s is already closed.\n" % branch)
        return

    rev = repo.branchtip(branch)
    newrev = context.memctx(repo, [rev, None], "Closed branch %s" % branch, [], None, opts.get('user'), opts.get('date'), extra={'close':1, 'branch':branch})
    newrev.commit()
    ui.status("Closed branch %s\n" % branch)

def switch_branch(ui, repo, branch, **opts):
    """Switch to the named branch"""
    if branch not in repo.branchtags():
        ui.warn("Branch %s does not exist! (use 'hg branches' to get a list of branches)\n" % branch)
        return
    curr = repo[None].branch()
    if branch == curr:
        ui.status("Already on branch %s\n" % branch)
        return
    hg.clean(repo, branch)

cmdtable = {
        "harvest": (harvest, [], "hg harvest BRANCH_NAME [TARGET_BRANCH]"),
        "close": (close_branch, [], "hg close BRANCH_NAME"),
        "switch": (switch_branch, [], "hg switch BRANCH_NAME"),
}

testedwith='2.4.1'

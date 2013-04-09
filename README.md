Branching - a Mercurial Plugin
==============================

This is a Mercurial plugin that enables simpler branch management. Because
named branches were only recently added, feature branch workflows that
rely heavly on named branches can use a little extra love.

Commands
========

harvest
-------

    $hg harvest BRANCH_NAME [TARGET_BRANCH]

Close the specified branch and merge it into the default branch, or the
named target branch. If the merge fails, you will need to resolve and
commit the merge manually.

close
-----

    $hg close BRANCH_NAME

Close the specified branch. This command does not affect your working
directory.

switch
------

    $hg switch BRANCH_NAME

Switch to the specified branch. This is essentially an alias of `hg update -C`.

branchdiff
----------

    $hg branchdiff BRANCH_NAME

Shows all the branch changes consolidated into a single diff. Technically this is a
diff between the branch creation point and the tip of the branch.

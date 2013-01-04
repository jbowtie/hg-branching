Branching - a Mercurial Plugin
==============================

This is a Mercurial plugin that enables simpler branch management. Because
named branches were only recently added, feature branch workflows that
rely heavly on named branches can use a little extra love.

Commands
========

harvest
-------

    $hg harvest BRANCH_NAME

Close the specified branch and merge it into the default branch. (Future
versions will allow you to specify the destination branch). If the merge fails,
you will need to resolve and commit the merge manually.

close
-----

    $hg close BRANCH_NAME

Close the specified branch.

switch
------

    $hg switch BRANCH_NAME

Switch to the specified branch. This is essentially an alias of `hg update -C`.

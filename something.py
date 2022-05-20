import sys
import os

from syncer import sync


def syncc(sourcedir, targetdir, action, **options):

    copier = sync(sourcedir, targetdir, action, **options)
    copier.do_work()

    # print report at the end
    copier.report()

    return set(copier._changed).union(copier._added).union(copier._deleted)
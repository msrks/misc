========================================
Read the Docs
========================================

開発手順
----------
githubからrepoをclone::

  $ git clone <github.repo>
  $ cd <project>

build-dirは無視したい::

  $ touch .gitignore
  $ echo docs/_build > .gitignore

docを作る::

  $ mkdir docs
  $ cd docs
  $ sphinx-quickstart

conf.pyを修正::

  html_theme = "defalut" に修正

githubにpush::

  $ cd ..
  $ git add -A
  $ git commit -m "[add] docs"
  $ git push

Read the Docs に登録して、<project>をimportしてbuild。

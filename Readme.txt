###############Google Docs ShareLink mit Stefan
https://docs.google.com/document/d/1aGwIvNbmDHOy7-iSW9quUbemvGnu29EU7zjeV2ZWX2o/edit?hl=de&pli=1





Git Ablauf
------------------------------------------------------------------------
1.  git init
------------------------------------------------------------------------
2. git status
------------------------------------------------------------------------
#########wenn code aktualisiert werden muss, dann erstmal stagen ###########
3. git add XXXXXgemäß statusXXXXX

------------------------------------------------------------------------
########dann commiten lokal#####################################
4. git commit -m "lokaler commit deines codes"

#####dann zum remote repository verknüpfen .. entweder es existiert noch nicht in github, dann musst du
echo "# BachelorProject_Ludwig_V2" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin "URL zum repository"
git push -u origin main


####falls du ein repository erstellt hast, dann musst du nur das machen:
git remote add origin "URL zum repository"
git branch -M main
git push -u origin main

------------------------------------------------------------------------
####zum schluss pushen an dein repositroy###############
5.git push -u origin main
User= MidgardSerpent
Pw= schaue auf github nach deinem personal access token in den settings deines profils


### dann bist du normalerweise fertig.
------------------------------------------------------------------------

###wenn du mal bullshit stagest, kannst du deinen stage auch wieder rückgängig machen,
zB bei der Klasse Optimizer_Code/TablePlotter.py:

git restore -s HEAD -SW Optimizer_Code/TablePlotter.py
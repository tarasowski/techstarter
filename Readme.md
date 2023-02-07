# Diff von Branches

- Ein wichtiger Aspekt von Git ist die Fähigkeit, mehrere Branches (Zweige) in
einem Projekt zu verwalten. Dies ermöglicht es Ihnen, mehrere Versionen Ihres
Codes parallel zu entwickeln und später zusammenzuführen.

- Wenn Sie Änderungen an Ihrem Code vornehmen, werden diese in dem Branch
gespeichert, auf dem Sie gerade arbeiten. Es ist jedoch häufig notwendig, die
Änderungen zwischen verschiedenen Branches zu vergleichen. Hier kommt die
Funktion git diff ins Spiel.

- Mit git diff können Sie die Änderungen zwischen zwei unterschiedlichen Branches
vergleichen. Dies kann hilfreich sein, wenn Sie sicherstellen möchten, dass alle
Änderungen, die Sie an einem Branch vorgenommen haben, auch in einem anderen
Branch vorhanden sind.

- Um die Änderungen zwischen zwei Branches zu vergleichen, können Sie den Befehl
git diff branchA branchB auf der Kommandozeile ausführen. Dies zeigt Ihnen eine
bersicht über alle Änderungen, die in branchA gemacht wurden, aber nicht in
branchB enthalten sind.

- Es ist wichtig zu beachten, dass Git Diffs nicht nur für den Vergleich von
Änderungen zwischen Branches nützlich sind, sondern auch für den Vergleich von
Änderungen zwischen zwei bestimmten Commit-IDs. Dies kann hilfreich sein, wenn
Sie Änderungen zu einem bestimmten Zeitpunkt in Ihrem Projekt verfolgen möchten.


# Diff von Branches 🌳 

### git diff branchA branchB

- Ein wichtiger Aspekt von Git ist die Fähigkeit, mehrere **Branches (Zweige)** in einem Projekt zu verwalten. Dies ermöglicht es Ihnen, mehrere Versionen Ihres Codes **parallel** zu entwickeln und später zusammenzuführen.

![](https://uploads.sitepoint.com/wp-content/uploads/2019/06/155993572204-gitflow.png)

Source: [sitepoint](https://rietta.com/blog/github-merge-types/)

- Es ist jedoch häufig notwendig, die Änderungen zwischen verschiedenen Branches zu **vergleichen**. Hier kommt die Funktion `git diff` ins Spiel.

- Dies kann hilfreich sein, wenn Sie sicherstellen möchten, dass alle Änderungen, die Sie an einem Branch vorgenommen haben, auch in einem anderen Branch vorhanden sind.

- Um die Änderungen zwischen zwei Branches zu vergleichen, können Sie den Befehl **git diff branchA branchB** (head-to-head) auf der Kommandozeile ausführen. 

### git diff commitA commitB

- Es ist wichtig zu beachten, dass Git Diffs nicht nur für den Vergleich von Änderungen zwischen Branches nützlich sind, sondern auch für den Vergleich von Änderungen zwischen zwei bestimmten **Commit-IDs**. 

- Dies kann hilfreich sein, wenn Sie Änderungen zu einem bestimmten **Zeitpunkt** in Ihrem Projekt verfolgen möchten.

![](https://d33wubrfki0l68.cloudfront.net/ee1b13e0aa1a7b67036df5f305389d5a9392f462/a3721/assets/blog/github-merge-types/merge-3.png)

Source: [rietto](https://riotta.com/blog/github-merge-types/)


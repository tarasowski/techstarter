# Was sind Git Diffs 🛠️

## git diff

- Git Diffs sind eine der wichtigsten Funktionen von Git und ermöglichen es Ihnen, **Änderungen** an Ihrem Code zu sehen. 

- Mit Git Diffs können Sie sehen, **was** in Ihren Dateien geändert wurde, seit Sie sie zuletzt gepusht oder gezogen haben.

- Um Git Diffs zu verwenden, können Sie den Befehl `git diff` auf der Kommandozeile ausführen. 

- Sie können Git Diffs auch für einen bestimmten **Branch** oder für einen bestimmten Zeitpunkt verwenden. 

```sh
git diff #shows the changes in your working tree relative to the last commit, only for tracked files
 
#tracked files are files that Git knows about. Untracked files are files not in your  staging area.

git diff HEAD #shows the changes in your working tree relative to the last commit (includes files that are not tracked)

git diff --staged #(or its synonym git diff --cached) shows the changes you staged for the next commit relative to the last commit
```

## git diff-highlight or diff-so-fancy

- Dies ist ein Skript, das die Lesbarkeit von Git Diffs verbessert, indem es die Änderungen in Farbe hervorhebt. 

- Dies kann sehr hilfreich sein, wenn Sie Änderungen **schnell** erkennen möchten, ohne den gesamten Diff-Text durchzusehen.

- Github / Gitlab UI

![](https://miro.medium.com/v2/resize:fit:640/format:webp/1*1Ctwbcei7JgxDakUJbzFug.png)

- Diff-so-fancy

![](https://user-images.githubusercontent.com/3429760/32387617-44c873da-c082-11e7-829c-6160b853adcb.png)

Source: [diff-so-fancy](https://github.com/so-fancy/diff-so-fancy)


1. Install diff-so-fancy
2. Stage files
3. Run git diff 


![](https://git-scm.com/book/en/v2/images/areas.png)

Source: [what is
         git](https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F)


## binary data 
- Es ist jedoch wichtig zu beachten, dass Git Diffs für binäre Daten **nicht so nützlich** sind wie für Textdateien, da die Änderungen nicht als Text angezeigt werden können.

- Wenn Sie mit binären Daten arbeiten, kann es schwierig sein, Git Diffs zu verwenden. (Git ist jedoch darauf ausgelegt, mit binären Daten umzugehen, und Sie können Git Diffs auch für binäre Daten verwenden.)




# VS Code vs Терминал

## Что удобно в VS Code

1. Панель Source Control - все изменённые файлы видны сразу, diff можно посмотреть в один клик.

2. Визуальный редактор merge-конфликтов - VS Code подсвечивает варианты («Accept Current», «Accept Incoming», «Accept Both») и позволяет разрешить конфликт в пару кликов.

3. GitLens / Git Graph - наглядная история коммитов, видно кто, когда и что менял, без `git log`.

## Что удобнее в терминале

1. Interactive rebase (`git rebase -i`) - в VS Code скрыто за UI, а в терминале полный контроль: pick, squash, fixup, drop, reword.
## task370

- https://algo-method.com/tasks/370/editorial

## メモ

### 狭義単調増加

x が大きくなると A[x]も大きくなる

## フロー

`left = 0`, `right = N - 1`

終了条件: `left == right`

## 注意点

前回までは結果に誤差が許されるものであったため、完璧に left と right が更新された状態`left == right`出なくても、答えが求められていましたが、今回は`left`, `right`の範囲が整数であるため、正しく更新をしないと無限ループに陥る可能性がある。

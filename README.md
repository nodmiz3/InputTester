# InputTester 1.0

マウス・キーボード入力測定ツール

## 機能

- 左クリック数
- 右クリック数
- CPS (Clicks Per Second)
- KPS (Keys Per Second)
- 最高CPS保存
- 最高KPS保存
- WASD統計
- Spaceキー統計
- Enterキー統計
- JSON履歴保存
- CSVエクスポート
- PyInstaller対応

## 操作

| キー | 動作 |
|-------|-------|
| R | リセット |
| C | CSV出力 |
| ESC | 終了 |

## ビルド

```bash
pip install -r requirements.txt
pyinstaller --onefile --windowed --icon=InputTester.ico --name=InputTester main.py
```

## ライセンス

MIT License

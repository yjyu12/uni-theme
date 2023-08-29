# ライブラリのインポート
import os
import glob
import pickle
import tfidf

# 変数の初期化
y = []  # ラベルを格納するリスト
x = []  # TF-IDFベクトルを格納するリスト

# ディレクトリ内のファイル一覧を処理する関数
file_test =  glob.glob('text/*.txt')
print(file_test)
def read_files(path, label):
    print("read_files=", path)
    # 指定されたパス内のテキストファイルの一覧を取得
    files = glob.glob(path + "/*.txt")
    print(files)
    for f in files:
        # LICENSE.txt ファイルは除外する
        if os.path.basename(f) == 'LICENSE.txt':
            continue
        # tfidf モジュールの add_file 関数でファイルを学習用に追加
        tfidf.add_file(f)
        # ラベルをリスト y に追加
        y.append(label)

# 各カテゴリのファイル一覧を読み込む
read_files('/Users/yamadaakira/Downloads/text\ /sports-watch', 0)  # スポーツ
read_files('/Users/yamadaakira/Downloads/text\ it-life-hack', 1)  # IT・ライフハック
read_files('/Users/yamadaakira/Downloads/text\ movie-enter', 2)  # 映画・エンタメ
read_files('/Users/yamadaakira/Downloads/text\ dokujo-tsushin', 3)  # 女性・恋愛

# ファイルを TF-IDF ベクトルに変換する
x = tfidf.calc_files()
print(x)

# 結果を保存する
pickle.dump([y, x], open('/Users/yamadaakira/Downloads/text\ genre.pickle', 'wb'))  # ラベルとベクトルを genre.pickle ファイルに保存
tfidf.save_dic('/Users/yamadaakira/Downloads/text\ genre-tdidf.dic')  # 辞書を genre-tdidf.dic ファイルに保存

# 処理が正常に完了したことを表示
print('ok')
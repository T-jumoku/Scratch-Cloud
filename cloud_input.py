import scratchattach as scratch3
import time

# 乗っ取られる危険性があるのでセッションIDは「「「絶対に」」」公開しないでください.
sessionID = "<session ID>"

session = scratch3.Session(sessionID, username="<your username>")

connection = session.connect_cloud(project_id="<project ID>") # <<<クォーテーションを外すのを推奨

print("クラウド変数に接続")

A = "<目的の値>" # <<<クォーテーションを外すのを推奨
connection.set_var("Request", A)
print(f"クラウド変数をセット {A}")
time.sleep(1)

# 参考にした記事
# https://note.com/penguin_282/n/na3c305e2d0b2
# https://note.com/penguin_282/n/n515746c7eead

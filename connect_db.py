import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


class ConnectDB:

    def __init__(self) -> None:
        # 環境変数からデータベース接続情報を取得
        self.dbhost = os.environ["DBHOST"]
        self.dbname = os.environ["DBNAME"]
        self.password = os.environ["PASSWORD"]
        self.dbuser = os.environ["DBUSER"]
        self.sslmode = os.environ["SSLMODE"]

    def get_connection_uri(self):
        # データベース接続URIを生成
        db_uri = f"""
            host={self.dbhost}
            dbname={self.dbname}
            user={self.dbuser}
            password={self.password}
            sslmode={self.sslmode}
        """
        return db_uri

    def get_connection_cls(self, db_uri):
        # データベース接続を確立
        conn = psycopg2.connect(db_uri)
        return conn


# try:
#     connect_db = ConnectDB()
#     conn_string = connect_db.get_connection_uri()
#     conn = connect_db.get_connection_cls(conn_string)
#     print("接続が確立されました")  # 接続成功メッセージ
#     cursor = conn.cursor()
#     print(type(conn))  # 接続オブジェクトの型を表示
#     print(type(cursor))  # カーソルオブジェクトの型を表示
#     print("OK")
# except Exception as e:
#     print(f"エラー: {e}")  # エラーメッセージを表示

from languages_selector import select_langs
import sqlite3
from os.path import expanduser

class DBHandler(object):

    _save_file  = expanduser("~")+"/.gyt.db"
    #criando base de dados
    _conn = sqlite3.connect(_save_file)
    _cursor = _conn.cursor()
    _exec_sql = _cursor.execute
    _save_sql = _conn.commit

    def __init__(self):
        #rotina de verificação inicial
        if not self.table_exists('langs'):
            self._cursor.execute("""
                CREATE TABLE langs (
                        lang TEXT NOT NULL,
                        url TEXT NOT NULL
                );
            """)
            self._save_sql()

        if not self.table_content('langs'):
            self.config_langs(first=1)

    def config_langs(self, first=0):
        langs = select_langs() if first else select_langs(self.table_content('langs'))
        self._exec_sql('DELETE FROM langs;')
        for key in langs:
            self._exec_sql(f"INSERT INTO langs VALUES ( '{key}', '{langs[key]}' )")
        self._save_sql()

    def table_exists(self, name):
        """
        Retorna 1 ou 0 se a tabela existe ou não.
        """
        sql = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{name}';"
        has_table = [e for e in self._exec_sql(sql)].__len__()
        return has_table

    def table_content(self, name):
        """
        Retorna conteúdo de uma tabela ou 0 se estiver vazio
        """
        sql = f"SELECT * FROM {name};"
        content = [e for e in self._exec_sql(sql)]
        if not content.__len__(): return 0
        return content

import oracledb

def drawing_table(data): 
    col_width = [max(len(str(row[i])) for row in data) for i in range(len(data[0]))]

    def draw_line(sep="+",fill="-"):
        return sep + sep.join(fill * (w + 2) for w in col_width) + sep
    
    print(draw_line())

    for i, row in enumerate(data):
        row_str = "| " + " | ".join(str(row[j]).ljust(col_width[j]) for j in range(len(row))) + " |"
        print(row_str)

    print(draw_line())


# Oracle XE 기본 접속 예제
dsn = "localhost:1521/XEPDB1"  # 호스트:포트/서비스명
conn = oracledb.connect(user="koreanraichu", password="testpass", dsn=dsn)
conn.autocommit = True
cursor = conn.cursor()

# cursor.execute("UPDATE POKEMON SET ANNOTATION='껍질포켓몬' WHERE dex_no=9")
# conn.commit()

cursor.execute("SELECT * FROM POKEMON WHERE FORM_CODE LIKE 'MEGA%' ORDER BY DEX_NO")
data = cursor.fetchall()

drawing_table(data)

cursor.close()
conn.close()

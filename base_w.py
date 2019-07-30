import sqlite3


def registration(ID):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ID FROM users')
    idin = cursor.fetchall()

    a = []
    for i in idin:
        a.append(i[0])

    if ID in a:
        pass
    else:
        cursor.execute('INSERT INTO users (ID, last_word, under_last_word) VALUES (?, ?, ?)', (ID, 'start', 'start'))

    conn.commit()
    cursor.close()
    conn.close()

def last_word(ID,word):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT last_word FROM users WHERE ID=:ID', {'ID':ID})
    idin = cursor.fetchone()
    a = idin[0]
    cursor.execute('UPDATE users SET last_word=:last_word, under_last_word=:under_last_word WHERE ID=:ID',
                   {'ID': ID, 'last_word': word, 'under_last_word':a})
    conn.commit()
    cursor.close()
    conn.close()

def save_type(word):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO magazine (type_p, is_done) VALUES (?, ?)', (word, 0))
    conn.commit()
    cursor.close()
    conn.close()

def save_undertype(word):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE magazine SET under_type=:under_type WHERE is_done=:is_done', {'is_done': 0, 'under_type': word})
    conn.commit()
    cursor.close()
    conn.close()

def save_title(word):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE magazine SET title=:title WHERE is_done=:is_done',
                   {'is_done': 0, 'title': word})
    conn.commit()
    cursor.close()
    conn.close()

def save_description(word):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE magazine SET description=:description WHERE is_done=:is_done', {'is_done': 0, 'description': word})
    conn.commit()
    cursor.close()
    conn.close()

def save_photo(word):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE magazine SET photo=:photo WHERE is_done=:is_done', {'is_done': 0, 'photo': word})
    conn.commit()
    cursor.close()
    conn.close()

def save_price(word):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE magazine SET price=:price WHERE is_done=:is_done', {'is_done': 0, 'price': word})
    conn.commit()
    cursor.close()
    conn.close()

def save_count(word):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE magazine SET count_=:count_ WHERE is_done=:is_done', {'is_done': 0, 'count_': word})
    cursor.execute('UPDATE magazine SET is_done=:is_done WHERE is_done=:is_done_', {'is_done': 1, 'is_done_': 0})
    conn.commit()
    cursor.close()
    conn.close()

def delete_none_products():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM magazine WHERE is_done=:is_done',
                   {'is_done': 0})
    conn.commit()
    cursor.close()
    conn.close()

def delete_tovar(ID):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM magazine WHERE ID=:ID', {'ID': ID})
    conn.commit()
    cursor.close()
    conn.close()

def adv_photo(photo, caption):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO advertisment (photo, caption) VALUES (?, ?)', (photo, caption))
    conn.commit()
    cursor.close()
    conn.close()

def adv_text( caption):
    photo = 'None'
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO advertisment (photo, caption) VALUES (?, ?)', (photo, caption))
    conn.commit()
    cursor.close()
    conn.close()

def all_tovar_info():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ID , title FROM magazine')
    idin = cursor.fetchall()
    word = ''
    conn.commit()
    cursor.close()
    conn.close()
    for i in idin:
        word += str(i[0])+ '. '+ str(i[1])+'\n'

    return  word

def update_tovar(ID, count):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE magazine SET count_=:count_ WHERE ID=:ID', {'ID': ID, 'count_': count})
    conn.commit()
    cursor.close()
    conn.close()

def take_last_word(ID):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT under_last_word , last_word FROM users WHERE ID=:ID',{'ID':ID})
    idin = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return idin[0], idin[1]


def searching_by(ID):
    l = take_last_word(ID)
    last_word_is = l[1]
    U_last_word_is = l[0]
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ID ,under_type, type_p, title FROM magazine')
    idin = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    id_is = 0
    tov = ''
    tov_list = []
    for i in idin:
            if i[1] == last_word_is:
                id_is = i[0]
                tov_list.append(i[0])
                tov = 'list'

    if len(tov_list) == 1:
        id_is = 0

    if id_is == 0:
        id_is = 0
        for i in idin:
            if (i[1] == last_word_is) and (i[2]== U_last_word_is):
                id_is = i[0]
                tov = 'Product'
                break

    if id_is == 0:
        id_is = 0
        for i in idin:
            if i[1] == last_word_is:
                id_is = i[0]
                tov = 'Product'
                break

    if id_is == 0:
        id_is = 0
        for i in idin:
            if i[3] == last_word_is:
                id_is = i[0]
                tov = 'Product'
                break

    if id_is == 0:
        return None
    else:
        if tov == 'Product':
            conn = sqlite3.connect('base.db')
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM magazine WHERE ID=:ID', {'ID':id_is})
            idn = cursor.fetchone()
            conn.commit()
            cursor.close()
            conn.close()
            a = []
            for i in idn:
                a.append(i)
            a.append(tov)
            return a
        elif tov == 'list':
            list_off = []
            for i in tov_list:
                conn = sqlite3.connect('base.db')
                cursor = conn.cursor()
                cursor.execute('SELECT * FROM magazine WHERE ID=:ID', {'ID': i})
                idn = cursor.fetchone()
                conn.commit()
                cursor.close()
                a = []
                for i in idn:
                    a.append(i)
                list_off.append(a)
            list_off.append('list')
            return list_off



def searching_by_title(title):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT ID FROM magazine WHERE title=:title', {'title': title})
    idn = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return idn[0]

def searching_by_title_1(title):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT count_ FROM magazine WHERE title=:title', {'title': title})
    idn = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return idn[0]

def save_trash(ID_p, count_, ID):
    ID = int(ID)
    ID_p = int(ID_p)
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT trash FROM users WHERE ID=:ID', {'ID': ID})
    trash = str(cursor.fetchone()[0]) + str(ID_p)+'+'+str(count_)+'&'
    cursor.execute('UPDATE users SET trash=:trash WHERE ID=:ID', {'ID': ID, 'trash': trash})
    conn.commit()
    cursor.close()
    conn.close()

def info_basket(ID):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT trash FROM users WHERE ID=:ID', {'ID': ID})
    idn = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return idn[0]


def title_from_ID(ID):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT title FROM magazine WHERE ID=:ID', {'ID': ID})
    idn = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return idn[0]

def searching_by_ID(ID):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT trash FROM users WHERE ID=:ID', {'ID': ID})
    info = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    spisok = info[4:].split('&')[:-1]
    nicks = []
    for i in range(len(spisok)):
        nicks.append([title_from_ID(int(spisok[i].split('+')[0])),spisok[i].split('+')[0]])
    return nicks

def delete_basket(ID, ID_p):
    ID_p = int(ID_p)
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT trash FROM users WHERE ID=:ID', {'ID': ID})
    info = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    spisok = info[4:].split('&')[:-1]
    new_spisok = 'None'
    for i in spisok:
        if ID_p != int(i.split('+')[0]):
            new_spisok += i+'&'

    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET trash=:trash WHERE ID=:ID', {'ID': ID, 'trash': new_spisok})
    conn.commit()
    cursor.close()
    conn.close()

def parse_ulw(ID):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT under_last_word FROM users WHERE ID=:ID', {'ID': ID})
    info = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return info


def update(user_id, phone):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET phone=:phone WHERE ID=:ID', {'phone': phone, 'ID': user_id})
    conn.commit()
    cursor.close()
    conn.close()

def price_from_ID(ID):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT price FROM magazine WHERE ID=:ID', {'ID': ID})
    idn = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return idn[0]

def price_info(ID):
    ID = int(ID)
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT trash FROM users WHERE ID=:ID', {'ID': ID})
    info = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    spisok = info[4:].split('&')[:-1]
    nicks = []


    for i in range(len(spisok)):
        ID_p = int(spisok[i].split('+')[0])
        count = spisok[i].split('+')[1]
        nicks.append([title_from_ID(ID_p), count , str(price_from_ID(ID_p))])

    return nicks


def set_phone(ID):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('SELECT phone FROM users WHERE ID=:ID', {'ID': ID})
    idn = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return idn[0]

def clear_basket(ID):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET trash=:trash WHERE ID=:ID', {'trash': 'None', 'ID': ID})
    conn.commit()
    cursor.close()
    conn.close()

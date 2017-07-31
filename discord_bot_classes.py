import pymysql.cursors
import pymysql
from credentials import USERNAME, PASS, DATABASE

def connection():
    conn = pymysql.connect(host='localhost', user=USERNAME, password=PASS, db=DATABASE, cursorclass=pymysql.cursors.DictCursor)

    return conn

def create_table_player_ranks():
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = 'CREATE TABLE players_ranks (discord_name VARCHAR(200), ingame_name VARCHAR(200),rank VARCHAR(200), rank_description LONGTEXT NULL)'
            cursor.execute(sql)
            print('Table players_ranks created')
    except pymysql.InternalError as e:
        if e.args[0] == 1050:
            print('Table players_ranks already exists')
    conn.close()

def create_table_player_ign():
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = 'CREATE TABLE players_ign (discord_name VARCHAR(200), ingame_name VARCHAR(200))'
            cursor.execute(sql)
            print('Table players_ign created')
    except pymysql.InternalError as e:
        if e.args[0] == 1050:
            print('Table players_ign already exists')
    conn.close()

def create_table_crafting_datasheet():
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = 'CREATE TABLE datasheet (discord_name VARCHAR(200), ingame_name VARCHAR(200), datasheet_url VARCHAR(200))'
            cursor.execute(sql)
            print('Table datasheet created')
    except pymysql.InternalError as e:
        if e.args[0] == 1050:
            print('Table datasheet already exists')
    conn.close()

def create_table_ranks():
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = 'CREATE TABLE ranks (rank_name VARCHAR(200), rank_description LONGTEXT NULL)'
            cursor.execute(sql)
            print('Table ranks created')
    except pymysql.InternalError as e:
        if e.args[0] == 1050:
            print('Table ranks already exists')
    conn.close()

def add_player_rank(discord_name, rank, rank_description):
    conn = connection()
    ingame_name = get_player_ingamename(discord_name)['ingame_name']
    if ingame_name is not None:
        try:
            with conn.cursor() as cursor:
                sql = "INSERT INTO players_ranks (discord_name, ingame_name, rank, rank_description) VALUES(%s, %s, %s, %s)"
                cursor.execute(sql, (discord_name, ingame_name, rank, rank_description))
                print('User ' + discord_name + ' added with the rank: ' + rank)
        except pymysql.InternalError as e:
            print(e.args[1] + ' at add_player_rank')
    else:
        print('InGameName Doesn\'t exist')
    conn.commit()
    conn.close()

def get_rank_description(rank):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT rank_description FROM ranks WHERE rank_name=%s"
            cursor.execute(sql, rank)
            rank_name = cursor.fetchone()
            if rank_name is not None:
                print(rank_name)
            return rank_name
    except pymysql.InternalError as e:
        print(e.args[1] + ' at get_rank_description')
    conn.close()


def add_rank_description(rank, rank_description):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO ranks (rank_name, rank_description) VALUES (%s, %s)"
            cursor.execute(sql, (rank, rank_description))
    except pymysql.InternalError as e:
        print(e.args[1] + ' at add_rank_description')
    conn.commit()
    conn.close()

def get_player_rank(member):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM players_ranks WHERE discord_name = %s"
            cursor.execute(sql, member)
            return cursor.fetchone()
    except pymysql.InternalError as e:
        print(e.args[1] + ' at get_player_rank')
    conn.close()

def get_datasheet(member):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM datasheet WHERE discord_name = %s"
            cursor.execute(sql, member)
            return cursor.fetchone()
    except pymysql.InternalError as e:
        print(e.args[1] + ' at get_datasheet')
    conn.close()

def add_datasheet(member, name, url):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO datasheet (discord_name, ingame_name, datasheet_url) VALUES (%s, %s, %s)"
            cursor.execute(sql, (member, name, url))
            print('Datasheet for user ' + member + 'added successfully')
    except pymysql.InternalError as e:
        print(e.args[1] + ' at add_datasheet')
    conn.commit()
    conn.close()

def get_player_ingamename(member):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = "SELECT ingame_name FROM players_ign WHERE discord_name = %s"
            cursor.execute(sql, member)
            return cursor.fetchone()
    except pymysql.InternalError as e:
        print(e.args[1] + ' at get_player_ign')
    conn.close()

def add_player_ingamename(member, ingame_name):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO players_ign (discord_name, ingame_name) VALUES (%s, %s)"
            cursor.execute(sql, (member, ingame_name))
            print('User ' + ingame_name + ' added successfully')
    except pymysql.InternalError as e:
        print(e.args[1] + ' at add_player_ign')
    conn.commit()
    conn.close()
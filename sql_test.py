#!/usr/bin/env python
# -*- coding: utf-8  -*-

import sqlCustom

sql = sqlCustom.MySQL(user = 'root', host = "localhost", passwd = "secret", db = "bike_test")
sql.ConnectDatabase()



print sql.execute("INSERT INTO `store` VALUES (2,'вул. Хмельницьке шосе (Лісопарк)'),(3,'вул.Соборна, 99'),(5,'Парк Дружбы Народов'),(6,'ХХХХХ');")
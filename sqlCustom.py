#!/usr/bin/env python
# -*- coding: utf-8  -*-

import MySQLdb

class MySQL:
    
    dbConnect = None
    cur = None
    host = None
    user = None
    passwd = None
    db = None
    serverName = 'mysql'
    charset = 'utf-8'
    
    def __init__(self, host, user, passwd, db):
        
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
       
        

    def ConnectDatabase(self):
        
        if self.serverName == 'mysql':
            self.dbConnect = MySQLdb.connect(host = self.host,
                         user = self.user,
                         passwd = self.passwd,
                         db = self.db)
        
        
        
        self.cur = self.dbConnect.cursor()

        
    def exec_mysql(self, string):
        
        #string = string.encode('utf-8') 
        self.cur.execute(string)
        
        
    def execute(self, request):
        if self.serverName == 'mysql':
            self.exec_mysql(request)
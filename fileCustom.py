#!/usr/bin/env python
# -*- coding: utf-8  -*-

class File:
    
    lines = []
    filename = ''
    file_res = None
    mode = ''
    lines_count = 0
    curr_line = 0
    
    def __init__(self, filename, mode = 'r+'):
        
        self.filename = filename
        self.mode = mode
        self.file_res = open(self.filename, self.mode)
        
        
    def get_count_lines(self):
        
        self.lines_count = 0
        
        for line in self.file_res:
            self.lines_count += 1
        
        self.file_res.seek(0)
            
        return self.lines_count
    
    def get_next_line(self):
        
        line = self.file_res.readline();
        self.curr_line += 1
        return line
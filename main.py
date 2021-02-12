from googleapi import google
import os
import time
import asyncio
dots = 1
num_page = 1
dp = 1
def ser(q, num_page):
    dots = 1
    search_results = google.search(q, num_page)
    while search_results == []:
        c()
        if dots == 0:
            print("Memuat Page")
        elif dots == 1:
            print("Memuat Page.")
        elif dots == 2:
            print("Memuat Page..")
        elif dots == 3:
            print("Memuat Page...")
            dots = -1
        dots += 1
        search_results = google.search(search, num_page)
    c()
    for result in search_results:
        print()
        print(result.name)
        print()
        print("description:",result.description)
        print()
        print("link:",result.link)
    print()
    print("page",num_page)
def c():
    os.system("clear")
while True:
    num_page = 1
    search = input("Google Search: ")
    print("Memuat...")
    search_results = google.search(search, num_page)
    while search_results == []:
        
        c()
        
        dots += 1 
        if dots == 0:
            print("Memuat Page")
        elif dots == 1:
            print("Memuat Page.")
        elif dots == 2:
            print("Memuat Page..")
        elif dots == 3:
            print("Memuat Page...")
            
            dots = -1
        search_results = google.search(search, num_page)
    c()
    for result in search_results:
        print()
        print(result.name)
        print()
        print("description:",result.description)
        print()
        print("link:",result.link)
    print()
    print("page:",num_page)
    while True:
        men2 = input(">")
        if men2 == "n":
            c()
            num_page = 1
            search = input("Google Search: ")
            print("Memuat...")
            search_results = google.search(search, num_page)
            while search_results == []:
                c()
                dots += 1 
                if dots == 0:
                    print("Memuat Page")
                elif dots == 1:
                    print("Memuat Page.")
                elif dots == 2:
                    print("Memuat Page..")
                elif dots == 3:
                    print("Memuat Page...")
                    dots = -1
                search_results = google.search(search, num_page)
            c()
            for result in search_results:
                print(result.name)
                print()
                print("description:",result.description)
                print()
                print("link:",result.link)
            print()
            print("page number:",num_page)
        elif men2 == "np":
            dp += 1
            ser(search, dp)
        elif men2 == "lp":
            if dp != 0:
                dp -= 1
                ser(search,dp)
            else:
                dp = dp
                ser(search, dp)
            

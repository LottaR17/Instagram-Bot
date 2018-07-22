#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.join(sys.path[0],'src'))

from instabot import InstaBot
from check_status import check_status
from feed_scanner import feed_scanner
from unfollow_protocol import unfollow_protocol
from follow_protocol import follow_protocol
import time


bot = InstaBot(login="Username", password="Password",
               like_per_day=500,
                media_max_like=100,
                media_min_like=10,
               comments_per_day=0,
               tag_list=['knitwear', 'menstyle', 'fashion', 'weddinginspiration', 'Antwerp', 'weddings', 'fashiongram', 'fashionphotography', 'scarfweather', 'travelingram', 'london', 'ootd', 'scarfweather', 'instagood ', 'amsterdam', 'girl', 'fashiondesign', 'fauxfur', 'cold', 'luxurylife', 'weddingday', 'winter', 'menswear', 'travel', 'snow', 'ice', 'inez', 'fashionlovers', 'luxury', 'allblack', 'fashionstyle', 'inezamsterdam', 'potd', 'followme', 'happy', 'traveldiaries', 'travelfashion', 'menwithstyle', 'weddinginspo', 'outfit', 'amsterdamcashmere', 'igers', 'wedding', 'fashionpost', 'scarvesfordays', 'luxuryfashion', 'weddingdress', 'fashionaddict', 'luxurylifestyle', 'look', 'inezboutique', 'scarfseason', 'mensfashion', 'menwithclass', 'weddingideas', 'cashmere', 'travelstyle', 'citylife', 'scarf'],
               user_blacklist={},
               max_like_for_one_tag=3,
               follow_per_day=500,
               follow_time=1*60,
               unfollow_per_day=500,
               unfollow_break_min=15,
               unfollow_break_max=30,
               log_mod=0,
               proxy='',
               # Use unwanted username list to block users which have username contains one of this string
               ## Doesn't have to match entirely example: mozart will be blocked because it contains *art
               ### freefollowers will be blocked because it contains free
               unwanted_username_list=['second','stuff','art','project','love','life','food','blog','free','keren','photo','graphy','indo',
                                       'travel','art','shop','store','sex','toko','jual','online','murah','jam','kaos','case','baju','fashion',
                                        'corp','tas','butik','grosir','karpet','sosis','salon','skin','care','cloth','tech','rental',
                                        'kamera','beauty','express','kredit','collection','impor','preloved','follow','follower','gain',
                                        '.id','_id','bags'])
while True:

    #print ("# MODE 0 = ORIGINAL MODE BY LEVPASHA")
    #print ("## MODE 1 = MODIFIKASI MODIFIKASI OLEH KEMONG")
    #print ("### MODE 2 = ORIGINAL MODE + UNFOLLOW SESEORANGTIDAK MENGIKUTI KEMBALI")
    #print ("#### MODE 3 = MODIFIKASI MODE: UNFOLLOW SESEORANG JIKA SESEORANG ITU TIDAK MENGIKUTI KEMBALI BERDASARKAN PADA FOLLOW YANG TERAKHIR SAJA")
    #print ("##### MODE 4 = MODIFIKASI MODE: IKUTI ORANG BERDASARKAN PADA FEED SAJA SAJA")
    #print ("###### MODE 5 = MODIFIKASI MODE: HANYA UNFOLLOW SETIAP ORANG, BAIK PENGGANDA ATAU TIDAK")
   
    ################################
           ##  WARNING   ###
    ################################

    # JANGAN GUNAKAN MODE 5 UNTUK PERIODE PANJANG. ANDA RISIKO AKUN ANDA DARI MENDAPATKAN BANNED
    ## GUNAKAN MODE 5 DALAM MODE BURST, GUNAKAN UNTUK MENGIKUTI ORANG SEBAGAI BANYAK YANG ANDA INGINKAN DALAM PERIODE WAKTU SINGKAT

    mode = 0

    #print("You choose mode : %i" %(mode))
    #print("CTRL + C to cancel this operation or wait 30 seconds to start")
    #time.sleep(30)

    if mode == 0 :
        bot.new_auto_mod()

    elif mode == 1 :
        check_status(bot)
        while bot.self_following - bot.self_follower > 200:
            unfollow_protocol(bot)
            time.sleep(10*60)
            check_status(bot)
        while bot.self_following - bot.self_follower < 400:
            while len(bot.user_info_list) <50 :
                feed_scanner(bot)
                time.sleep(5*60)
                follow_protocol(bot)
                time.sleep(10*60)
                check_status(bot)

    elif mode == 2 :
        bot.bot_mode = 1
        bot.new_auto_mod()

    elif mode == 3 :
        unfollow_protocol(bot)
        time.sleep(10*60)

    elif mode == 4 :
        feed_scanner(bot)
        time.sleep(60)
        follow_protocol(bot)
        time.sleep(10*60)

    elif mode == 5 :
        bot.bot_mode=2
        unfollow_protocol(bot)

    else :
        print ("Wrong mode!")

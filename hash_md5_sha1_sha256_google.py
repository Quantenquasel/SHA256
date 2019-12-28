# -*- coding: utf-8 -*-
"""
@Autor: Andreas Kölblin
"""
import webbrowser
import hashlib
repeat = True
while repeat:
    passwd = input("Bitte geben Sie ein Passwort ein, dessen Hashwerte MD5, SHA1 und SHA256 ermittelt werden soll: ")
    print("MD5: " + hashlib.md5(passwd.encode('utf-8')).hexdigest())
    print("SHA1: " + hashlib.sha1(passwd.encode('utf-8')).hexdigest())
    print("SHA256: " + hashlib.sha256(passwd.encode('utf-8')).hexdigest())
    print("Das Ergebnis der Googlesuche mit dem MD5/SHA1 und SHA256-Hash des Passwortes sollte jetzt angezeigt werden.")
    m5 = hashlib.md5(passwd.encode('utf-8')).hexdigest()
    sha1 = hashlib.sha1(passwd.encode('utf-8')).hexdigest()
    sha256 = hashlib.sha256(passwd.encode('utf-8')).hexdigest()
    ur="https://www.google.com/#q="
    webbrowser.open_new(ur+m5)
    webbrowser.open_new_tab(ur+sha256) # Neuen Tab öffnen
    webbrowser.open_new_tab(ur+sha1)
    repeat = input("Zum Beenden 'Enter'und um ein weiteres Passwort zu prüfen bitte eine beliebige Taste drücken.")

import streamlit as st
import mysql.connector


def conectar_banco():
    conn = mysql.connector.connect(
        host="mysql.railway.internal", 
        user="root",
        password="rZfgEyBBGafsSzBCLFRJvXIUBIqoHpOw",
        database="railway"
    )
    return conn
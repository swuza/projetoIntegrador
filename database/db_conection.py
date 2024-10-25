import streamlit as st
import mysql.connector


def conectar_banco():
    conn = mysql.connector.connect(
        host="localhost", 
        user="root",
        password="",
        database="captacao"
    )
    return conn
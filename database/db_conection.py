import streamlit as st
from sqlalchemy import create_engine


def conectar_banco():
    conn = create_engine(
        'postgres:HhEWwioNxQYtNWznhmnKxjViFwihrwSy@postgres.railway.internal:5432/railway'
    ).connect()
    return conn
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /projetoIntegrador

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD streamlit run main.py

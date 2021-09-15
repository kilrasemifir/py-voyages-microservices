FROM python

COPY requierments.txt requierments.txt

RUN pip install -r requierments.txt

COPY src/ src/

CMD ["python", "app.py"]
FROM python

WORKDIR /movie

COPY movie.py .

CMD ["python","movie.py"]


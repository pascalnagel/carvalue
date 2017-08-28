FROM python:3
ADD carvalue_api.py /
RUN pip3 install xgboost
CMD [ "python", "./carvalue_api.py" ]

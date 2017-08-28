FROM python:3
ADD carvalue_api.py /
RUN pip3 install -r python_package_requirements.txt
CMD [ "python", "./carvalue_api.py" ]

FROM python:3
ADD carvalue_api.py /
ADD python_package_requirements.txt /
RUN pip3 install --no-cache-dir -r python_package_requirements.txt
CMD [ "python", "./carvalue_api.py" ]

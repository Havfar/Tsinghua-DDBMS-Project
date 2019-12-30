# Distributed Database Systems with Hadoop

The goal of this project was to get familiar to the techniques used to handle big data in a distributed environment. We have seen at how to create a distributed database using Hadoop HDFS, Yarn, Mapreduce and Apache Hive, and how one can use them in a simple newspaper/blog application. We found that our setup could easily support the small amount of data (40 GB) we threw at it, but that the use of Hive with MapReduce was quite slow to handle the data creation from the application. Because of this we also saw the importance of using a cache to improve performance. 

This project was create by Håvard Farestveit and Tobias Skjelvik as a course project for  Distributed Database Systems at Tsinghua University

## Tech/Framework used

* Hadoop (HDFS, Yarn, MapReduce)
* Apache Hive w/PyHive
* Flask
* React.js
* Microsoft Azure

## Installation 

### Clone repo

```bash
git clone https://github.com/Havfar/Tsinghua-DDBMS-Project.git
```

```bash
cd Tsinghua-DDBMS-Project
pip install -r requirements.txt

cd dbms-client
npm install
```

## Usage

### Start DBMS 1 and DBMS 2

```
cd Tsinghua-DDBMS-Project
python dmbs1.py
python dbms2.py
```

### Start client

```python
cd dbms-client/
npm start
```

### Monitoring the running status

We are using the build in monitor in Hadoop to get an overview of the status to the cluster. It can be seen at http://23.99.116.151:50070/dfshealth.html#tab-overview
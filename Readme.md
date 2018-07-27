# How Install and How to run a simple script to import MySql data into Tensorflow

## What is the TensorFlow?

TensorFlow is an open source software library for numerical computation using data-flow graphs. It was originally developed by the Google Brain Team within Google's Machine Intelligence research organization for machine learning and deep neural networks research, but the system is general enough to be applicable in a wide variety of other domains as well. It reached version 1.0 in February 2017, and has continued rapid development, with 21,000+ commits thus far, many from outside contributors. Its open source community.

## Getting Started


### Prerequisites

```
sudo yum -y install epel-release
sudo yum -y install gcc gcc-c++ python-pip python-devel atlas atlas-devel gcc-gfortran openssl-devel libffi-devel
pip install --upgrade virtualenv
virtualenv --system-site-packages ~/venvs/tensorflow
source ~/venvs/tensorflow/bin/activate
pip install --upgrade numpy scipy wheel cryptography #optional
pip install --upgrade https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.10.0rc0-cp35-cp35m-linux_x86_64.whl
 ```
or below if you want gpu, support, but cuda and cudnn are required, see docs for more install instructions
 ```
 pip install --upgrade https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow-0.10.0rc0-cp35-cp35m-linux_x86_64.whl
```


### Installing

Installing TensorFlow on Ubuntu with Virtualenv
You can follow this link 
```
https://www.tensorflow.org/install/install_linux
```
Installing TensorFlow on macOS
You can follow this link 
```
https://www.tensorflow.org/install/install_mac
```
Installing TensorFlow on Windows
You can follow this link 
```
https://www.tensorflow.org/install/install_windows
```
## Running script
```
(tensorflow) michelone-Mac:tensorflow root# python3 Mysql2Tf.py 
```
### Result

```
Query executed for database.table

Wrote 547855 rows to csv.



[array([b'2016-05-11 23:00:00', b'1', b'3032', b'514', b'IN', b'583',

       b'12850', b'2', b'2dac2b64ceeb4143ad425bd7f411d96c', b'320x50',

       b'1.18', b'1400', b'1400', b'802', b'73',

       b'0.94719001650810240000', b'4'], dtype=object)]

[array([b'2016-05-11 23:00:00', b'1', b'3032', b'514', b'IN', b'583',

       b'14375', b'2', b'2dac2b64ceeb4143ad425bd7f411d96c', b'320x50',

       b'1.18', b'1562', b'1562', b'925', b'54',

       b'1.10398003458976750000', b'3'], dtype=object)]

[array([b'2016-05-11 23:00:00', b'1', b'3032', b'514', b'IN', b'583',

       b'1917', b'2', b'2dac2b64ceeb4143ad425bd7f411d96c', b'320x50',

       b'1.18', b'2031', b'2031', b'1189', b'116',

       b'1.40652002394199370000', b'4'], dtype=object)]

[array([b'2016-05-11 23:00:00', b'1', b'3032', b'514', b'IN', b'583',

       b'2461', b'2', b'2dac2b64ceeb4143ad425bd7f411d96c', b'320x50',

       b'1.18', b'1759', b'1759', b'1182', b'60',

       b'1.40653999894857400000', b'0'], dtype=object)]

[array([b'2016-05-11 23:00:00', b'1', b'3032', b'514', b'IN', b'583',

       b'49052', b'2', b'2dac2b64ceeb4143ad425bd7f411d96c', b'320x50',

       b'1.18', b'3263', b'3263', b'1908', b'137',

       b'2.25145010650157930000', b'10'], dtype=object)]

[array([b'2016-05-11 23:00:00', b'1', b'3185', b'514', b'IN', b'583',

       b'1299', b'2', b'agltb3B1Yi1pbmNyDAsSA0FwcBiipaIVDA', b'320x480',

       b'0.15', b'6', b'6', b'2', b'0', b'0.00327000010292977100', b'0'],

      dtype=object)]

[array([b'2016-05-11 23:00:00', b'1', b'3185', b'514', b'IN', b'583',

       b'1299', b'2', b'agltb3B1Yi1pbmNyDAsSA0FwcBiipaIVDA', b'320x480',

       b'1.97', b'21', b'21', b'8', b'1', b'0.01672000065445900000', b'0'],

      dtype=object)]

[array([b'2016-05-11 23:00:00', b'1', b'3185', b'514', b'IN', b'583',

       b'1299', b'2', b'agltb3B1Yi1pbmNyDAsSA0FwcBiipaIVDA', b'320x480',

       b'4.58', b'42', b'42', b'0', b'0', b'0E-20', b'0'], dtype=object)]

[array([b'2016-05-11 23:00:00', b'1', b'3185', b'514', b'IN', b'583',

       b'13063', b'2', b'agltb3B1Yi1pbmNyDAsSA0FwcBiipaIVDA', b'320x480',

       b'0.15', b'7', b'7', b'1', b'0', b'0.00025000001187436280', b'0'],

      dtype=object)]

[array([b'2016-05-11 23:00:00', b'1', b'3185', b'514', b'IN', b'583',

       b'13063', b'2', b'agltb3B1Yi1pbmNyDAsSA0FwcBiipaIVDA', b'320x480',

       b'1.97', b'22', b'22', b'2', b'0', b'0.00425000023096799850', b'0'],

      dtype=object)]
```


## Authors

* **Michele Berardi** -- [MicheleBerardi](https://github.com/micheleberardi)

* Please feel free to reach out with any questions



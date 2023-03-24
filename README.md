### QMENTA implementation of dcm2niix

Build it  
```shell
docker build -t nvii/qmenta-dcm2niix-private:4.0 .
```
Tag it  
```shell
docker tag nvii/qmenta-dcm2niix-private:4.0 nvii/qmenta-dcm2niix-public:2.0
```
Push it  
```shell
docker push nvii/qmenta-dcm2niix-public:2.0
```
Test it  
```shell
python test_container_sdk.py --settings settings.json --values settings_values.json nvii/qmenta-dcm2niix-private:4.0 data/input data/output/
```

Docker Hub repo [here](https://hub.docker.com/r/nvii/qmenta-dcm2niix-public).
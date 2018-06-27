##### 简单的读取CSV文件到MySQL

##### 存储的MySQL
```
CREATE TABLE `ip_store` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `from_ip` bigint(20) NOT NULL,
  `to_ip` bigint(20) NOT NULL,
  `country` varchar(255) DEFAULT NULL,
  `province` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `from_ip` (`from_ip`) USING BTREE,
  KEY `to_ip` (`to_ip`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=10813024 DEFAULT CHARSET=utf8;
```

##### 国外免费的IP库地址，可下载CSV文件
https://db-ip.com/db/


ps:ip地址在MySQL中用long类型存储
mysql中IP转long的函数
```
SELECT INET_ATON('1.1.0.230')
SELECT INET_NTOA(16785408)
```
查询IP区间的语句
```
SELECT * FROM ip_store WHERE from_ip <= INET_ATON('1.1.73.0') AND to_ip >=  INET_ATON('1.1.73.0');
```

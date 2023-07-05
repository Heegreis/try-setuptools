# try-setuptools

setup name 使用底線，pip list 裡面也會顯示為 `-` 號。駝峰式命名不會有影響。
基本運作方式: 自動將 project root directory 下的資料夾(package)都打包起來，直接放在 root 底下的 python 檔不會被打包。
name 和 package 名稱可以不一樣。實際在 import 時要使用 package 名稱 import。

若是 src-layout，直接放在 src 底下的 python 檔會被打包。因為指定了 src 資料夾，所以 root 底下的 package 不會被打包。

# Foodies-List-Website

## 完整實現CRUD功能的網站，讓使用者可以讀取、新增、修改和刪除餐廳資訊。
-------------
![image](https://github.com/kenHsieh25053/Foodies-List-Website/blob/master/foodies%20indexpage.PNG)
-------------

## 主要架構:
前後端透過API傳遞資料，實現前後端分離。
### 後端
+ django-rest-framework
+ sqlite
+ corsheaders 處理跨域請求問題套件
+ webpack_loader 將django 和 vue 整合在一起

### 前端
+ vue.js
+ vue-bootstrap

## 後端API接口
API                               | 用途          
----------------------------------|:--------------
api/restaurants/create/           | 新增文章
api/restaurants/list/             | 列出所有文章
api/restaurants/update/<int:pk>/  | 更新文章By Pk值 
api/restaurants/delete/<int:pk>/  | 刪除文章By Pk值

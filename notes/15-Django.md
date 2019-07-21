# Django

安装：pip install django==1.8.2

创建django项目：diango-admin starproject test1

该框架与其他框架不同，其他大多是基于mkv 而django是基于mkt框架，django框架分为三大块：模型、视图、模板

## django 开发过程：

1. 创建虚拟环境 mkvirtualenv vdjango
2. 安装django 包：pip install django==1.8.2
3. 创建项目文件：django-admin startproject django_test
4. 添加应用：python mange.py startapp booktest
5. 创建模型：在models中根据设计好的表创建类，并添加相关属性
6. 创建视图：在view中创建视图获取模型类中内容，并建立路由链接解析正则，配置起路由作为作为web的回应，需要使用到request
7. 创建模板：单独创建一个目录名为templates 在创建一个子目录为book_test 然后在其目录中创建html文件，修改urls配置识别模板位置
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

解决django pyhton3版本不能导入mysql-python数据库模块办法：

* 安装pymysql、mysqlclient 两个包
* 在环境下找如下路径：/.virtualenvs/vdjango/lib/python3.6/site-packages/django/db
* 修改\__init__.py 文件，添加：

```
import pymysql
pymysql.install_as_MySQLdb()
```

## 模型

在模型中定义属性，会生成数据库的表字段，在定义属性时不用定义ID主键，djiango会自动增加主键列。

### 命名规则：

​	不能是python保留关键字、不能使用连续的下划线（由django的查询方式决定）

### 定义属性

导入包：from django.db import models

常用属性：IntegerField/BooleanField/CharField/DateField/DateTimeField

关系属性：ForeignKey(一对多)、ManyToManyField(多对多)、OneToOneField(一对一)

### 访问关系：

建立两个表：BookInfo 、HeroInfo

- 用一访问多：对象.模型类小写_set

```
bookinfo.heroinfo_set
```

- 用一访问一：对象.模型类小写

```
heroinfo.bookinfo
```

- 访问id：对象.属性_id

```
heroinfo.book_id
```

### 元选项

定义Meta类设置表的名称

```
class BookInfo(models.Model):
    ...
    class Meta():
        db_table="bookinfo"
        
```

### 建立模型详细解析

使用 python manage.py startapp booktest建立应用并在seting中添加

```
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)
class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo')
```

然后执行python manage.py makemogrations,生成迁移文件

python mange.py migrate 完成迁移生成数据库表

运行python manage.py shell

导入BookInfo模块

使用:

```
b=BookInfo()
b.object.all() 查询全部数据
```

- objects：是Manager类型的对象，用于与数据库进行交互
- 当定义模型类时没有指定管理器，则Django会为模型类提供一个名为objects的管理器
- 支持明确指定模型类的管理器

可以自己定义管理器。主要从定义get_queryset方法

```
class BookInfoManager(models.Manager):
    def get_queryset(self):
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)
class BookInfo(models.Model):
    ...
    books = BookInfoManager()
```



在使用过程中由于创造数据过于繁琐，所以可以在上述建立的管理类中创建方法

如下：

```
class BookInfoManager(models.Manager):
    def create_book(self, title, pub_date):
        book = self.model()
        book.btitle = title
        book.bpub_date = pub_date
        book.bread=0
        book.bcommet=0
        book.isDelete = False
        return book

class BookInfo(models.Model):
    ...
    books = BookInfoManager()
调用：book=BookInfo.books.create_book("abc",datetime(1980,1,1))
保存：book.save()
```

## 模型的查询

- 查询集表示从数据库中获取的对象集合
- 查询集可以含有零个、一个或多个过滤器
- 过滤器基于所给的参数限制查询的结果
- 从Sql的角度，查询集和select语句等价，过滤器像where和limit子句

### 查询的方法

- all()
- filter()
- exclude()
- order_by()
- values()：一个对象构成一个字典，然后构成一个列表返回

### 比较运算符

- exact：表示判等，大小写敏感；如果没有写“ 比较运算符”，表示判等

```
filter(isDelete=False)
```

- contains：是否包含，大小写敏感

```
exclude(btitle__contains='传')
```

- startswith、endswith：以value开头或结尾，大小写敏感

```
exclude(btitle__endswith='传')
```

- isnull、isnotnull：是否为null

```
filter(btitle__isnull=False)
```

- 在前面加个i表示不区分大小写，如iexact、icontains、istarswith、iendswith
- in：是否包含在范围内

```
filter(pk__in=[1, 2, 3, 4, 5])
```

- gt、gte、lt、lte：大于、大于等于、小于、小于等于

```
filter(id__gt=3)
```

- year、month、day、week_day、hour、minute、second：对日期间类型的属性进行运算

```
filter(bpub_date__year=1980)
filter(bpub_date__gt=date(1980, 12, 31))
```

### 关联关系的查询：处理join查询

- 语法：模型类名 <属性名> <比较>
- 注：可以没有__<比较>部分，表示等于，结果同inner join
- 可返向使用，即在关联的两个模型中都可以使用

```
filter(heroinfo_ _hcontent_ _contains='八')
```

### 聚合函数

```
from django.db.models import Max
maxDate = list.aggregate(Max('bpub_date'))
```

- count的一般用法：

```
count = list.count()
```

#### F对象

- 可以使用模型的字段A与字段B进行比较，如果A写在了等号的左边，则B出现在等号的右边，需要通过F对象构造

```
list.filter(bread__gte=F('bcommet'))
```

#### 象

- 过滤器的方法中关键字参数查询，会合并为And进行
- 需要进行or查询，使用Q()对象
- Q对象(django.db.models.Q)用于封装一组关键字参数，这些关键字参数与“比较运算符”中的相同

```
list.filter(pk_ _lt=6).filter(bcommet_ _gt=10)
list.filter(Q(pk_ _lt=6) | Q(bcommet_ _gt=10))
```

## 视图

### URLconf

* 在setting.py文件中能配置根url 通过配置变量：ROOT_URKCONF
* 配置路由信息在项目目录下配置urls.py文件在urlpatterns中添加应用中的urls文件的地址使用include模块在url函数中完成

```
from django.conf.urls import include, url
urlpatterns = [
    url(r'^', include('booktest.urls', namespace='booktest')),
]
```

* 在路由配置过程中符合正则表达式的匹配模式

```
http://www.itcast.cn/python/1/?i=1&p=new，只匹配“/python/1/”部分
```

* 正则表达式在使用过程中其分组’（）‘的作用在路由中是用来传递参数的，起到获取数据传递到视图中，在视图中第一的函数需要设置形参来接收参数

```
url(r'^([0-9]+)/$', views.detail, name='detail'),
```

* 在视图中有post请求时可以采用在视图中使用装饰器@csrf_exempt来释放禁止请求

```python
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def ajax1(request):
    usename = UserInfo.manage.all()
    print(list(usename.values()))
    return JsonResponse({"data":list(usename.values())})
    
    
 #也可以在模板中form中添加{% csrf_token %}
```

* URL反向解析如果在视图中需要使用地址时，当使用硬编码时会出现当url发生改变就不能识别现在的路由地址，因而使用反向解析就能解决这个问题，

在视图中导入django.core.urlresolvers.reverse

使用reverse函数能通过路由配置的name 就能直接动态生成地址信息

```python
def logout(request):
    request.session.flush()
    return redirect(reverse('index:test3'))

```

## 视图错误响应

- Django原生自带几个默认视图用于处理HTTP错误

- defaults.page_not_found(request, template_name='404.html')
- 默认的404视图将传递一个变量给模板：request_path，它是导致错误的URL
- 如果Django在检测URLconf中的每个正则表达式后没有找到匹配的内容也将调用404视图
- 如果在settings中DEBUG设置为True，那么将永远不会调用404视图，而是显示URLconf 并带有一些调试信息
- 在templates中创建404.html

有404 500 400响应等视图

# HttpReqeust对象

- 服务器接收到http协议的请求后，会根据报文创建HttpRequest对象
- 视图函数的第一个参数是HttpRequest对象
- 在django.http模块中定义了HttpRequest对象的API

- 下面除非特别说明，属性都是只读的
- path：一个字符串，表示请求的页面的完整路径，不包含域名
- method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'
- encoding：一个字符串，表示提交的数据的编码方式
- 如果为None则表示使用浏览器的默认设置，一般为utf-8
- 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值

- GET：一个类似于字典的对象，包含get请求方式的所有参数
- POST：一个类似于字典的对象，包含post请求方式的所有参数
- FILES：一个类似于字典的对象，包含所有的上传文件
- COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串
- session：一个既可读又可写的类似于字典的对象，表示当前的会话，只有当Django 启用会话的支持时才可用，详细内容见“状态保持”

## GET属性

- QueryDict类型的对象

- 包含get请求方式的所有参数

- 与url请求地址中的参数对应，位于?后面

- 参数的格式是键值对，如key1=value1

- 多个参数之间，使用&连接，如key1=value1&key2=value2

- 键是开发人员定下来的，值是可变的

- 示例如下

- 创建视图getTest1用于定义链接，getTest2用于接收一键一值，getTest3用于接收一键多值

- ```
  def getTest2(request):
      a=request.GET['a']
      b=request.GET['b']
      context={'a':a,'b':b}
      return render(request,'booktest/getTest2.html',context)
      #一键多值
   def getTest3(request):
      a=request.GET.getlist('a')
      b=request.GET['b']
      context={'a':a,'b':b}
      return render(request,'booktest/getTest3.html',context)
  ```

## POST属性

- QueryDict类型的对象
- 包含post请求方式的所有参数
- 与form表单中的控件对应
- 并且在js中也可请求post方法
- 在表单中使用name 来对用 **’键** ‘使用value来对应 **键值** 
- 请求是在表单中方使用{% csrf_token %}来屏蔽控件的限制连接

## HttpResponse对象

对象为django.http模块中定义了HttpResponse对象的API

在使用时不需要调用模板可直接返回数据即可

```
#coding=utf-8
from django.http import HttpResponse

def index(request):
    return HttpResponse('你好')
```

也可使用模板

```
from django.template import RequestContext, loader

def index(request):
    t1 = loader.get_template('polls/index.html')
    context = RequestContext(request, {'h1': 'hello'})
    return HttpResponse(t1.render(context))
```

#### HttpResponseRedirect

- 重定向，服务器端跳转
- 构造函数的第一个参数用来指定重定向的地址

#### 子类JsonResponse

- 返回json数据，一般用于异步请求
- *_init* _(data)
- 帮助用户创建JSON编码的响应
- 参数data是字典对象
- JsonResponse的默认Content-Type为application/json

#### render

- render(request, template_name[, context])
- 结合一个给定的模板和一个给定的上下文字典，并返回一个渲染后的HttpResponse对象
- request：该request用于生成response
- template_name：要使用的模板的完整名称
- context：添加到模板上下文的一个字典，视图将在渲染模板之前调用它

#### 重定向rediret

- redirect(to)
- 为传递进来的参数返回HttpResponseRedirect
- to推荐使用反向解析

`from django.shortcuts import render, redirect`

## 状态保持

状态保持一般提供了两种方式分别为cookie、session

- 实现状态保持的方式：在客户端或服务器端存储与会话有关的数据
- 对于数据的安全要求高的建议使用session方式，该方式时将数据缓存到服务器端，使用唯一的session_id来识别，防止其他用户盗用
- 方式cookie方式是直接缓存在本地的客户端

### session

- 启用会话后，每个HttpRequest对象将具有一个session属性，它是一个类字典对象
- get(key, default=None)：根据键获取会话的值
- clear()：清除所有会话
- flush()：删除当前的会话数据并删除会话的Cookie
- del request.session['member_id']：删除会话

```
def index(request):
    uname = request.session.get('uname')
    return render(request, 'booktest/index.html', {'uname': uname})

def login(request):
    return render(request, 'booktest/login.html')

def login_handle(request):
    request.session['uname'] = request.POST['uname']
    return redirect(reverse('main:index'))
```

会话时间配置

- set_expiry(value)：设置会话的超时时间
- 如果没有指定，则两个星期后过期
- 如果value是一个整数，会话将在values秒没有活动后过期
- 若果value是一个imedelta对象，会话将在当前时间加上这个指定的日期/时间过期
- 如果value为0，那么用户会话的Cookie将在用户的浏览器关闭时过期
- 如果value为None，那么会话永不过期
- 修改视图中login_handle函数，查看效果

#### 使用Redis缓存session

- 会话还支持文件、纯cookie、Memcached、Redis等方式存储，下面演示使用redis存储

导入包：pip install django-redis-sessions

在settings中配置如下项

```
SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = ''
SESSION_REDIS_PREFIX = 'session'
```

### redis的使用方法

```
启动：sudo redis-server /etc/redis/redis.conf
停止：sudo redis-server stop
重启：sudo redis-server restart
redis-cli：使用客户端连接服务器
keys *：查看所有的键
get name：获取指定键的值
del name：删除指定名称的键
```

## 定义模板标签

模板语言包括

- 变量
- 标签 { % 代码块 % }
- 过滤器
- 注释{# 代码或html #}



### 语法：{ % tag % }

- for标签

```javascript
{ %for ... in ...%}
循环逻辑
{{forloop.counter}}表示当前是第几次循环
{ %empty%}
给出的列表为或列表不存在时，执行此处
{ %endfor%}
```

- if标签

```
{ %if ...%}
逻辑1
{ %elif ...%}
逻辑2
{ %else%}
逻辑3
{ %endif%}
```

- comment标签

```
{ % comment % }
多行注释
{ % endcomment % }
```

- include：加载模板并以标签内的参数渲染

```
{ %include "foo/bar.html" % }
```

- url：反向解析

```
{ % url 'name:name2' p1 p2 %}
```

- csrf_token：这个标签用于跨站请求伪造保护

```
{ % csrf_token %}
```

#### 过滤器

- 语法：{ { 变量|过滤器 }}，例如{ { name|lower }}，表示将变量name的值变为小写输出
- 使用管道符号 (|)来应用过滤器
- 通过使用过滤器来改变变量的计算结果
- 可以在if标签中使用过滤器结合运算符

## 模板继承

- 模板继承可以减少页面内容的重复定义，实现页面内容的重用
- 典型应用：网站的头部、尾部是一样的，这些内容可以定义在父模板中，子模板不需要重复定义
- block标签：在父模板中预留区域，在子模板中填充
- extends继承：继承，写在模板文件的第一行
- 定义父模板base.html

```
{ %block block_name%}
这里可以定义默认值
如果不定义默认值，则表示空字符串
{ %endblock%}


使用定义好的模板
{ % extends "base.html" %}

在子模板中填充内容
{ %block block_name%}
实际填充内容
{ %endblock%}
注意子模板与父模板中的标签名字要相同
```

## HTML转义

在正常情况下模板会将用户输入的字符原封不动的输出如\<h1>hello\</h1> 输出同样为\<h1>hello\</h1>

- html转义，就是将包含的html标签输出，而不被解释执行，原因是当显示用户提交字符串时，可能包含一些攻击性的代码，如js脚本
- Django会将如下字符自动转义：

```
< 会转换为&lt;

> 会转换为&gt;

' (单引号) 会转换为&#39;

" (双引号)会转换为 &quot;

& 会转换为 &amp;
```

但是在一些情况下需要输出对应不被转义的效果那么就使用

{{data|safe}}来声明该data数据为安全数据不用转义

也可以使用

```
{ % autoescape off %}
{{ body }}
{ % endautoescape %}
```

在autoescape标签之间的变量或字符串都不会被转义

## csrf

- 全称Cross Site Request Forgery，跨站请求伪造

- 某些恶意网站上包含链接、表单按钮或者JavaScript，它们会利用登录过的用户在浏览器中的认证信息试图在你的网站上完成某些操作，这就是跨站攻击

  - 在django的模板中，提供了防止跨站攻击的方法，使用步骤如下：
  - step1：在settings.py中启用'django.middleware.csrf.CsrfViewMiddleware'中间件，此项在创建项目时，默认被启用
  - step2：在csrf1.html中添加标签

  ```
  <form>
  {% csrf_token %}
  ...
  </form>
  ```

  - 如果某些视图不需要保护，可以使用装饰器csrf_exempt，模板中也不需要写标签，修改csrf2的视图如下

  ```
  from django.views.decorators.csrf import csrf_exempt
  
  @csrf_exempt
  def csrf2(request):
      uname=request.POST['uname']
      return render(request,'booktest/csrf2.html',{'uname':uname})
      
  ```
  
## 中间件

* 是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改Django的输入或输出

  * 激活：添加到Django配置文件中的MIDDLEWARE_CLASSES元组中
  * 每个中间件组件是一个独立的Python类，可以定义下面方法中的一个或多个
    - *_init* _：无需任何参数，服务器响应第一个请求的时候调用一次，用于确定是否启用当前中间件
    - process_request(request)：执行视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
    - process_view(request, view_func, view_args, view_kwargs)：调用视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
    - process_template_response(request, response)：在视图刚好执行完毕之后被调用，在每个请求上调用，返回实现了render方法的响应对象
    - process_response(request, response)：所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
    - process_exception(request,response,exception)：当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象

- 使用中间件，可以干扰整个处理过程，每次请求中都会执行中间件的这个方法
- 示例：自定义异常处理
- 与settings.py同级目录下创建myexception.py文件，定义类MyException，实现process_exception方法

## 上传图片

- 当Django在处理文件上传的时候，文件数据被保存在request.FILES
- FILES中的每个键为<input type="file" name="" />中的name
- 注意：FILES只有在请求的方法为POST 且提交的<form>带有enctype="multipart/form-data" 的情况下才会包含数据。否则，FILES 将为一个空的类似于字典的对象
- 使用模型处理上传文件：将属性定义成models.ImageField类型

## 分页

Paginator(列表,int)：返回分页对象，参数为列表数据，每面数据的条数

#### 属性

- count：对象总数
- num_pages：页面总数
- page_range：页码列表，从1开始，例如[1, 2, 3, 4]

#### 方法

- page(num)：下标以1开始，如果提供的页码不存在，抛出InvalidPage异常

#### 异常exception

- InvalidPage：当向page()传入一个无效的页码时抛出
- PageNotAnInteger：当向page()传入一个不是整数的值时抛出
- EmptyPage：当向page()提供一个有效值，但是那个页面上没有任何对象时抛出

```
from django.core.paginator import Paginator

def pagTest(request, pIndex):
    list1 = AreaInfo.objects.filter(aParent__isnull=True)
    p = Paginator(list1, 10)
    if pIndex == '':
        pIndex = '1'
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range
    return render(request, 'booktest/pagTest.html', {'list': list2, 'plist': plist, 'pIndex': pIndex})
```

## 使用Ajax

- 使用视图通过上下文向模板中传递数据，需要先加载完成模板的静态页面，再执行模型代码，生成最张的html，返回给浏览器，这个过程将页面与数据集成到了一起，扩展性差
- 改进方案：通过ajax的方式获取数据，通过dom操作将数据呈现到界面上
- 推荐使用框架的ajax相关方法，不要使用XMLHttpRequest对象，因为操作麻烦且不容易查错
- jquery框架中提供了$.ajax、$.get、$.post方法，用于进行异步交互
- 由于csrf的约束，推荐使用$.get
- 示例：实现省市区的选择
- 最终实现效果如图：

![city.gif](https://i.loli.net/2019/08/05/cY9PUHQlICLme76.gif)

#### 修改settings.py关于静态文件的设置

```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
```

#### 在models.py中定义模型

```
class AreaInfo(models.Model):
    aid = models.IntegerField(primary_key=True)
    atitle = models.CharField(max_length=20)
    aPArea = models.ForeignKey('AreaInfo', null=True)
```

#### 在views.py中编写视图

- index用于展示页面
- getArea1用于返回省级数据
- getArea2用于根据省、市编号返回市、区信息，格式都为字典对象

```
from django.shortcuts import render
from django.http import JsonResponse
from models import AreaInfo

def index(request):
    return render(request, 'ct1/index.html')

def getArea1(request):
    list = AreaInfo.objects.filter(aPArea__isnull=True)
    list2 = []
    for a in list:
        list2.append([a.aid, a.atitle])
    return JsonResponse({'data': list2})

def getArea2(request, pid):
    list = AreaInfo.objects.filter(aPArea_id=pid)
    list2 = []
    for a in list:
        list2.append({'id': a.aid, 'title': a.atitle})
    return JsonResponse({'data': list2})
```

#### 在模板中引入jquery文件

#### 编写js代码

- 绑定change事件
- 发出异步请求
- 使用dom添加元素



## 富文本编辑器

- 借助富文本编辑器，管理员能够编辑出来一个包含html的页面，从而页面的显示效果，可以由管理员定义，而不用完全依赖于前期开发人员
- 此处以tinymce为例，其它富文本编辑器的使用可以自行学习
- 使用编辑器的显示效果为

## 缓存

- 对于中等流量的网站来说，尽可能地减少开销是必要的。缓存数据就是为了保存那些需要很多计算资源的结果，这样的话就不必在下次重复消耗计算资源
- Django自带了一个健壮的缓存系统来保存动态页面，避免对于每次请求都重新计算
- Django提供了不同级别的缓存粒度：可以缓存特定视图的输出、可以仅仅缓存那些很难生产出来的部分、或者可以缓存整个网站

#### 设置缓存

- 通过设置决定把数据缓存在哪里，是数据库中、文件系统还是在内存中
- 通过setting文件的CACHES配置来实现
- 参数TIMEOUT：缓存的默认过期时间，以秒为单位，这个参数默认是300秒，即5分钟；设置TIMEOUT为None表示永远不会过期，值设置成0造成缓存立即失效



## 全文检索

- 全文检索不同于特定字段的模糊查询，使用全文检索的效率更高，并且能够对于中文进行分词处理
- haystack：django的一个包，可以方便地对model里面的内容进行索引、搜索，设计为支持whoosh,solr,Xapian,Elasticsearc四种全文检索引擎后端，属于一种全文检索的框架
- whoosh：纯Python编写的全文搜索引擎，虽然性能比不上sphinx、xapian、Elasticsearc等，但是无二进制包，程序不会莫名其妙的崩溃，对于小型的站点，whoosh已经足够使用
- jieba：一款免费的中文分词包，如果觉得不好用可以使用一些收费产品

# celery

- [官方网站](http://www.celeryproject.org/)
- [中文文档](http://docs.jinkan.org/docs/celery/)
- 示例一：用户发起request，并等待response返回。在本些views中，可能需要执行一段耗时的程序，那么用户就会等待很长时间，造成不好的用户体验
- 示例二：网站每小时需要同步一次天气预报信息，但是http是请求触发的，难道要一小时请求一次吗？
- 使用celery后，情况就不一样了
- 示例一的解决：将耗时的程序放到celery中执行
- 示例二的解决：使用celery定时执行
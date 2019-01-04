# 异常处理

在需要长时间运行的代码使用

```
try:


except:

```

来处理程序避免程序遇到一些问题直接崩溃

## 多异常捕获

通过在expect后面添加异常的名字来捕获异常

```
try:
	xx
except NameError:
	xx
except FileNotFoundError:
	xx
```

通过写出多个选项来捕获异常，当异常产生时就会根据异常信息来找到对应的except实现通知我们。

同时也可以

```
try:
	xx
except (NameError,FileNotFoundError):#在python3中需要添加括号，在2中不需要括号
	xx
```

在这个怎么知道产生什么异常呢？

使用：

```
except NameError as f:
	print("一个时是异常是％s"%f)
except （NameError,FileNotFoundError） asf:
	print("有多个异常处理时是％s"%f)

```

捕获所有异常（当不确定什么异常时

```
except Exception as f:
	print("不定义捕获的异常是：％s"%f)
```

Exception代表的是异常的类，也就是可以捕获在之中的全部异常并且输出

```
except:
	xx
else:
	xx
```

else作用就是没有发生异常时执行else中的内容

## 异常try.....finally:

```
except Exception as f:
	print("不定义捕获的异常是：％s"%f)
finally:
	xx
```

在finally中的内容不管有没有异常也执行，有没有捕获到异常等等都会执行finally中的内容。

## 异常传递

```
def text1():#函数中有一场

def text2():函数二中无异常，调用　函数一
def text3():函数三无异常，调用函数一
```

也就是函数异常传递就是谁调用该异常所在函数就将异常传递到调用函数，在调用的函数中使用try....except     Exception as f:就可以将异常传递过来

## 抛出自定义异常　

这个就是自己定义一个异常对象，然后在程序　中通过raise来抛出也就是产生异常

```
class Test(Exception):
	def __init__(self,length,atleast):
		self.length = length
		self.atleast = atleast
try:
	raise Test(1,3)
except Test as f:
	print("异常是：",f.length,f.atleast)
```

在继承对象时必须是Exception这个对象下

## 抛出异常

```
except Exception as f:
	if a>2:
		print(f)
	else:
		raise  #后面什么也不加代表直接抛出捕获到的异常

```

这样抛出异常，就会让系统来处理，这样可以用在某种允许存在出错次数范围之类的判别
class Person():
	def __getattribute__(self,obj):
		print("---test--")
		if obj.startswith("a"):
			return "hahaha"
		else:
			return self.test
	def test(self):
		print("heihei")

t = Person()
print("t.a")
t.a

print("t.b")

t.b


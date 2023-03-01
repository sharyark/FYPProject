from db import DBhelper



obj = DBhelper()

# obj.addEmployee("shasdah","alskdjfl@gmail.com")
# obj.exit(123)

x = obj.sameDate("2023-02-01")[0][2]
for i in str(x):
    print(i,end="")
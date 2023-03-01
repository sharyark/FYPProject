import mysql.connector
import time
from datetime import datetime
class DBhelper:

    try:
        def __init__(self):
            self.conn = mysql.connector.connect(host='localhost',user='root',password='',database='employee')
            self.mycursor = self.conn.cursor()
            # print(self.conn)
    except:
        print("some error occured")

    else:
        print("connected successfully")
        

    def entrance(self,I_D):
        # try:
            # print('above executinggg')
            # self.mycursor.execute("INSERT INTO `employees` (`id`, `name`, `employee_id`, `created_at`) VALUES (29, 'skar0ya', '1318', current_timestamp());")
        data = self.check_email(I_D) #data is fetched from registered table
        # print(data)

        if(len(data)):
            # print('im in len in data')
            same_date = self.chk_in_attendance(str(time.strftime("%Y-%m-%d")),data[0][0])
            # print("---\n",same_date,"---\n")
            # data_attendance = self.chk_in_attendance(str(time.strftime("%Y-%m-%d")),data[0][0])
            if not len(same_date):
                self.mark_attendance(data)
                print("i am calling marking attendance")
            else:
                print('i am in else of mark calling')
                # if(len(same_date)):
                tm = self.synchronise(same_date)
                print('im in of in tm is :',tm)
                if tm > 2:
                    print('count updating is called :',tm)
                    self.update_count(same_date)
        else:
            print('person is not registered..')

    def exit(self,e_id):
        data = self.check_email(e_id)
        # print(data)
        id = data[0][0]
        print(id)
        self.mark_exist(id)
        
        
        
        
        # try:
        #     print('above executinggg')
        #     # self.mycursor.execute("INSERT INTO `employees` (`id`, `name`, `employee_id`, `created_at`) VALUES (29, 'skar0ya', '1318', current_timestamp());")
        #     data = self.check_email(e_id)
        #     print(datetime.now())
        #     now = datetime.now()
        #     current_time = now.strftime("%H:%M:%S")
        #     print('--------------')
        #     print(current_time)
        #     if len(data):
        #         self.mycursor.execute("""UPDATE `attendance` SET `ex_time` = '{}',`eflag` ='0', `lflag`='1';""".format(current_time))
        #         self.conn.commit()
        #         print('createdd ....')
        #     else:
        #         print("you already created by this name")
        # except:
        #     # return -1
        #     print('some error occured')
        # else:
        #     print('insertd successfully')
        #     return 1
  
 
    def check_email(self,name): #this function check registered person in database 
            # print(name)
            self.mycursor.execute("""
            select * from registered where name like '{}'""".format(name))
            data = self.mycursor.fetchall()
            return data
    
    def fetch_date(self,i_d):
        self.mycursor.execute("""
        select * from registered where name like '{}'""".format(name))
        data = self.mycursor.fetchall()
        return data
    
    def sameDate(self,e_id):
            self.mycursor.execute("""
            select * from attendance where _date like '{}'""".format(e_id))
            data = self.mycursor.fetchall()
            return data
    
    def check_first_time(self,i_d):

        self.mycursor.execute("""select * from attendance
          where e_id like '{}'""".format(i_d))
        data = self.mycursor.fetchall()
        print("------b----")
        print(data)
        print(data[0][6])
        print('------l------')
        print(data)
        return data
    
    def mark_exist(self,e_id):
        try:
            print('above executinggg')
            _date = time.strftime("%Y-%m-%d")
            data = self.chk_in_attendance(_date,e_id)
            print(datetime.now())
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print('--------------')
            print(current_time)
            if len(data):
                self.mycursor.execute("""UPDATE `attendance` 
                SET `ex_time` = '{}',`eflag` ='0', `lflag`='1'
                WHERE _date like '{}';""".format(current_time,_date))
                self.conn.commit()
                print('createdd ....')
            else:
                print("you already created by this name")
        except:
            # return -1
            print('some error occured')
        else:
            print('insertd successfully')
            return 1

    def chk_in_attendance(self,date_,i_d):
        self.mycursor.execute("""
            select * from attendance where _date = '{}' AND e_id = '{}'""".format(date_,i_d))
        data = self.mycursor.fetchall()
        # print(data)
        return data

    def update_count(self,data):
        # print("---------before update---------")
        # print(data)
        e_id = data[0][0]
        last_count = data[0][6]
        date_ = data[0][1]
        new_count = int(last_count)
        new_count +=1
        now = datetime.now()
        n_time = now.strftime("%H:%M:%S")
        self.mycursor.execute("""UPDATE attendance SET entry_count={},e_time='{}'
        WHERE _date LIKE '{}';""".format(new_count,n_time,date_))
        self.conn.commit()
        # self.mycursor.execute("""UPDATE attendance SET e_time='{}';""".format(n_time))
        # data = self.mycursor.fetchall()
        # print('---------after update--------')
        # data = self.chk_in_attendance(data[0][2],e_id)
        # print(data)
        # print(data[0][1])
    
    def mark_attendance(self,data,eflag=1,lflag=0):
        # try:
        # e_id = data[0][0]
        try:
            e_id = data[0][0]
            _date = time.strftime("%Y-%m-%d")
            now = datetime.now()
            e_time = now.strftime("%H:%M:%S")
            self.mycursor.execute("""INSERT INTO `attendance` ( `e_id`, `_date`, `e_time`, `eflag`, `lflag`,`entry_count`)
            VALUES ( '{}', '{}', '{}', '{}', '{}',{});""".format(e_id,_date,e_time,eflag,lflag,0))
            self.conn.commit()
            print('createdd ....')
        except:
            print('some error occured')
            return -1
        else:
            print('insertd successfully............')
            return 1

    def synchronise(self,data):
        p_time = data[0][2]
        print('----------------------')
        print(data)
        # print(p_time.year)
        p_time = str(p_time).split(':')
        p_h,p_m = int(p_time[0]),int(p_time[1])
        now = datetime.now()
        n_time = now.strftime("%H:%M:%S")
        n_time = str(n_time).split(':')
        n_h,n_m = int(n_time[0]),int(n_time[1])
        d_h = n_h - p_h
        d_m = n_m - p_m
        if d_h:
            if d_h <=2:
                return 3
            else:
                return d_h
        else:
            return d_m
        # print(d_h,d_m)
        # print(time.time()-p_time)
        # print(n_m,p_m)
        # print(n_h-p_h,n_m-p_m)
        # print('-----------------------')
        # return n_m-p_m













#       # registration
#     def register(self,name,email,password):
#        try:
#          self.mycursor.execute("""INSERT INTO `login` (`id`, `name`, `email`, `password`)
#          VALUES (NULL, '{}', '{}', '{}'); """.format(name,email,password))
#          self.conn.commit()
#        except:
#             return -1
#        else:
#             return 1

#     # searching..
#     def search(self,email,password):
#         self.mycursor.execute("""
#         select * from login where email like '{}' and password like '{}'""".format(email,password))
#         data = self.mycursor.fetchall()
#         return data
# # obj = DBhelper()


# exit function implementation copy
#  def exit(self,e_id):

#         # print(datetime.now())
#         # now = datetime.now()
#         # current_time = now.strftime("%H:%M:%S")
#         # print('--------------')
#         # print(current_time)
#         try:
#             print('above executinggg')
#             # self.mycursor.execute("INSERT INTO `employees` (`id`, `name`, `employee_id`, `created_at`) VALUES (29, 'skar0ya', '1318', current_timestamp());")
#             data = self.check_email(e_id)
#             print(datetime.now())
#             now = datetime.now()
#             current_time = now.strftime("%H:%M:%S")
#             print('--------------')
#             print(current_time)
#             if len(data):
#                 self.mycursor.execute("""UPDATE `attendance` SET `ex_time` = '{}',`eflag` ='0', `lflag`='1';""".format(current_time))
#                 self.conn.commit()
#                 print('createdd ....')
#             else:
#                 print("you already created by this name")
#         except:
#             # return -1
#             print('some error occured')
#         else:
#             print('insertd successfully')
#             return 1
  
 
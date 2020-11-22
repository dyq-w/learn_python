'''

全班级的个人信息：

{
    128 ：{
                'name': None,
                'idCard': None,
                'sex': None,
                'class': None,
                'attendance record':{

                    'dady1': 'YES',
                    'dady2': None,
                    'dady3': None,
                    'dady4': None,
                    'dady5': None,
                    'dady6': None,
                    'dady7': None,
                    'dady8': None,
                    
                    }
             
            }

    129： {
                'name': None,
                'idCard': None,
                'sex': None,
                'class': None,
                'attendance record':{

                    'dady1': None,
                    'dady2': None,
                    'dady3': None,
                    'dady4': None,
                    'dady5': None,
                    'dady6': None,
                    'dady7': None,
                    'dady8': None,
                    
                    }
             
            }

}



'''

import json

per_info = {
    'name': None,
    'idCard': None,
    'sex': None,
    'class': None,
    'attendance record':{

        'dady1': None,
        'dady2': None,
        'dady3': None,
        'dady4': None,
        'dady5': None,
        'dady6': None,
        'dady7': None,
        'dady8': None,
        
        }
 
}




class StuSys():

    def __init__(self):

        self.file = 'stu_info.json'
        

    def load_json(self):#将stu_info.json序列化
    

        f = open(self.file)

        stu_info =json.load(f)

        f.close()

        return stu_info

    def dump_json(self, obj):#将信息保存到stu_info.json

        f = open(self.file, 'w')

        stu_info =json.dump(obj,f)

        f.close()

    def input_info(self): #录入同学基本信息

        idCard = input('学号:')
        name = input('请输入姓名：')
        sex = input(f'请输入{name}同学的性别：')
        class_ = input(f'请输入{name}同学的班级：')
        
        result = {
            
            'name': name,
            'idCard': idCard,
            'sex': sex,
            'class': class_,
            'attendance record':{

                'dady1': None,
                'dady2': None,
                'dady3': None,
                'dady4': None,
                'dady5': None,
                'dady6': None,
                'dady7': None,
                'dady8': None,
            
            }
             
        }

        return result


    def save_json(self, per_info):#保存个人信息

        #取出stu_info.json是信息

        stu_info = self.load_json() #取出信息

        idCard = per_info['idCard']

        stu_info.update({idCard: per_info})

        self.dump_json(stu_info)#保存信息

        print(f"{per_info['name']}个人信息保存完毕！！！")

    def input_per_info_save_json(self): #输入个人信息并保存


        self.save_json(self.input_info())
        

    def attendance_record(self):#输入学号更改考勤

        info = self.load_json()#反向序列化信息
        
        idCard = input('请输入考勤的学号：')

        day = input('请输入要更改的日期：')
        
        ch_value = input('请输入考情结果：')

        info[idCard]['attendance record'].update({f'dady{day}': ch_value})

        self.dump_json(info) #将修改后的info保存到指定位置
    


    def attendance_record_(self):#输入姓名更改考勤

        info = self.load_json()#反向序列化信息

        print(info)
        
        name = input('请输入考勤的姓名：')

        for i in info.values():

            if name == i['name']:

                stu_info = i

        

        day = input('请输入要更改的日期：')
        
        ch_value = input('请输入考情结果：')

        stu_info['attendance record'].update({f'dady{day}': ch_value})

        self.dump_json(info) #将修改后的info保存到指定位置




    def stu_perinfo_seek(self):#查询功能输出，全部学生的信息

        info = self.load_json()

        print('\t\t\t\t 全部学生的信息')

        print('姓名\t学号\t性别\t班级\tday1\tday2\tday3\tday4\tday5\tday6\tday7\tday8')

        
        for i in info.values():

             print('{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t'.format(i.get('name'), i.get('idCard'), i.get('sex'), i.get('class') ,
                                                                    i['attendance record'].get('dady1'),i['attendance record'].get('dady2'),
                                                                    i['attendance record'].get('dady3'),i['attendance record'].get('dady4'),
                                                                    i['attendance record'].get('dady5'),i['attendance record'].get('dady6'),
                                                                    i['attendance record'].get('dady7'),i['attendance record'].get('dady8'),))
            



    
        

    def main(self):
        

        print('*******欢迎来到xx学生考勤系统********')

        while True:
            print('说明：输入 1添加同学基本信息，输入 2给同学打卡,输入 3显示所有信息 没有输入为退出 ')
            val = input('请选择功能：')

            if val == '1':

                self.input_per_info_save_json()

                print('信息写入完成')
            elif val == '2':

                val2 = input('输入1为输入学号打卡，输入2为输入同学姓名打卡:')

                if val2 == '1':

                    self.attendance_record()
                else:

                    self.attendance_record_()

                print('打卡成功')

            elif val == '3':


                   self.stu_perinfo_seek()


                   
            else:
                
                print('退出系统')
                break

        

                
                
            

if __name__ == '__main__':#主程序入口

   
    StuSys().main()

    

    
    



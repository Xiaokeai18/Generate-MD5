#coding:utf-8
import hashlib

#########测试#################
m = hashlib.md5()
m.update(b"hello")
m.update(b"world")
print(m.hexdigest())  #fc5e038d38a57032085441e7fe7010b0
m1 = hashlib.md5()
m1.update(b"helloworld")
print(m1.hexdigest()) #fc5e038d38a57032085441e7fe7010b0
print('All of the above output should be fc5e038d38a57032085441e7fe7010b0')
if m1.hexdigest()=='fc5e038d38a57032085441e7fe7010b0' and m.hexdigest()=='fc5e038d38a57032085441e7fe7010b0':
    print('Test: Sussess! Ready to work.\n')
##########测试完毕#############
    '''
    generate md5 of file
    '''
    m2 = hashlib.md5()

    f = open("D:\My_File\lianbo.json", "rb")
    data = f.read(1024)
    while data:
        m2.update(data)
        data = f.read(1024)
    print(m2.hexdigest())  

else:
    print('Test: Error!')

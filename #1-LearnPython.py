# coding=utf-8
#-----上行使注释支持中文,必须放在第一行!

# 1-指定章节
part = input("Please input which part to run  :")
part = float(part)
# submine不安装插件就不支持input
# 2-手动章节
#part = 8

while True:
    if part == 1:
        print("\n\n----1.基本输入输出部分---------------------------")
        print("----Eg1: Hello world!!!!!")
        print("----Eg2: （中英混合测试）计算结果100+200= ",100+200)  #注意python2中没有括号，有了会中文出错，P3没事儿
        print(
            '''
            Python2与 Python3的区别：
            print满足3个条件（带参数 + 带括号 + python2）==》中文显示不正常''')
        print(''' ----Eg3: 三引号的的用法：
            可以随意的排列中间的格式。''')
        
        print("\n----Eg4: input:")
        a1 = input("Eg3: a1 is ? :")  # 注意！input默认为字符串型
        print("a1 is : " , a1)
        #print(unicode("请输入销售额", encoding="utf-8"), a1)
        a1 = int(a1)  # a1为字符，要转换为整数型
        if a1 >= 0:  # a1 不能为字符
            print(a1)
        else:
            print(-a1)
        break


    if part == 1.1:
        print("\n\n----1.1.1 基本输入输出部分: list-----------------------")

        list1 = [0, 1, 2, 3, 4, 5, 6, 7, "word1", "word2"]  # ---list的定义方法
        print("list1:", list1[::2])
        print("list1:", list1[2:10:2])  # ----从第2个元素开始打印至第10个元素,每隔2个打印一次

        print("\n\n----1.1.2 list comprehensions,列表生成式--------------")
        list2 = [i**2 for i in range(1, 10) if i**2 % 2 == 0]
        print("list2:", list2)
        print("\n\n----1.1.3 list comprehensions,列表生成式--------------")
        #2.1列表生成式其实是一种循环的简化版,但是python更崇尚上面的简单的代码
        list3 = []  # 空列表
        for i3 in range(1, 10):
            if i3**2 % 2 == 0:
                list3.append(i3 ** 2)  # 不断的在列表后加元素
        print("list3:", list3)

        break

    if part == 1.2:
        print("\n\n----基本输入输出部分: 字典 dict----------------------------")

        dict1 = {
            1: "one",
            2: "two",
            3: "three",
            None: "none"
        }  # ---dict字典的定义方法
        print(dict1[1])  # ---从dict取得某一元素

        print(1 in dict1)  # ----判断dict里有没有指定元素
        print("one" in dict1)  # -----只判断左边,不判断右边
        print("one" not in dict1)

        print(dict1.get(1111, "如果没有1111这个元素,就打印这里的语句"))  # -----字典的"get"函数

        break

    if part == 2:
        print("\n\n----2.1 while循环函数")
        i = 0
        while True:
            i = i + 1
            if i == 1:
                print("i == 1")
            if i == 2:  # ----continue 是跳回循环开始
                print("i == 2,skipping 2")
                continue
            if i == 3:
                print("i == 3")
            if i == 4:  # ----break 是结束当前循环
                print("i == 4,will break")
                break
            if i == 5:
                print("We will never see it")


        print("\n\n----2.2 for 循环----for迭代")
        spring = ["hello", "world", "is", "simple"]  # ----"列表"的定义方式
        for word in spring:  # -----"for"循环的使用方式
            print(word + "!!!")

        break

    if part == 3:
        print("\n\n----1.函数部分:普通函数调用---------")
        # 定义函数，别忘了冒号，
        print("Def the FUNCTION")
        def myf_1(xf1, n):
            '''docstring的用法:文档字符串

            功能：该函数时限x的n次方的输出.'''
            '''
            170930：《ABOP》惯例写法:
                首行以大写字母开始，句号结尾。
                第二行是空行；
                从第三行开始是详细的描述；
                强烈建议你在你的函数中使用文档字符串时遵循这个惯例
                调用docstring方式：help(myf_1).
            '''
            temp = 1
            while n > 0:
                n = n - 1
                temp = temp * xf1
                print("temp is", temp)
                print("n is", n)
            print("IN the myf_1 ,The final temp is ", temp)
            return temp

        x1 = input("Please int the x1 :")
        x1 = int(x1)  # input默认是字符型,要转化为int型
        x2 = input("Please int the x2 :")
        x2 = int(x2)
        print('FUN is ', myf_1(x1, x2))


        print("\n\n----2.函数部分:递归函数----------")
        # 在函数中调用自身
        def myf_2(n_mf2):  # ----例子:递归函数计算阶乘fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
            if n_mf2 == 1:
                return 1
            return n_mf2 * myf_2(n_mf2 - 1)
        print("递归函数的结果:")
        print(myf_2(5))


        print("\n\n----3.函数部分:可变参数(*args,**kwargs)----------")
        #*args表示任何多个无名参数，它是一个tuple
        #**kwargs表示关键字参数，它是一个dict字典
        def f_args(*args, **kwargs):
            print("args", args)
            print("kwargs", kwargs)
            print("--------------")
            return
        f_args(1, 2, 3)
        f_args(1, 2, 3, a=1, b="b", c="c")  # 注意这种混合输入,哪些归args,哪些属于kwargs
        break

    if part == 3.1:
        print("\n\n----高级函数部分----------")
        print("\n\n----3.1 高阶函数(可以调用其他函数的函数)----------")
        def myf_add(x, y, f):
            return f(x) + f(y)  # 注意这个f参数的位置,它代替了函数名称的位置
        # ---绝对值函数名"abs"传给了参数f,这样就直接在函数内部调用了abs函数
        print("abs(3)+abs(5)= ", myf_add(3, 5, abs))


        print("\n\n----3.2 map() 函数----------")
        #---map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
        #------list:由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
        def mapstarget(x):  # 定义一个平方的函数
            return x * x
        l = []
        # --这里map函数将后面的序列依次输入fun函数中,依次得出结果
        l = list(map(mapstarget, [1, 2, 3, 7, 8, 9]))
        print(l)


        print("\n\n----3.3 reduce函数 (未完成)----------")
        pass


        print("\n\n----3.4.filter() 函数---------------")
        # 和map()类似，filter()也接收一个函数和一个序列。
        # 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
        def f_is_odd(n):
            return n % 2 == 1  # --函数作用:如果是奇数就返回"1"
        l = list(filter(f_is_odd, [1, 2, 3, 7, 8, 9]))  # 返回1的奇数都被留下来了
        # list:返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。
        print(l)


        print("\n\n----3.5 sorted() 函数----------")
        # 1---按照绝对值对列表排序
        print(sorted([36, 5, -12, 9, -21], key=abs))
        # 2---按照分数或者名字对字典里的分数排序
        L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
        def by_name(t):
            return t[0]

        def by_score(t):
            return t[1]
        print(sorted(L, key=by_score))  # --注意这里,key用的是自己编写的函数,来决定按成绩排序还是按姓名排序


        print("\n\n----3.6 匿名函数:lambda----------")
        # Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。
        #lambda x: x * x
        # 实际上就是:
        # def f(x):
        #   return x * x
        break


    if part == 3.2:
        print("\n\n----3.7 返回函数-----------------")
        # 一个函数可以返回一个计算结果，也可以返回一个函数

        def lazy_sum(*args):
            def real_sum():
                sumx = 0
                for n in args:
                    sumx = sumx + n
                return sumx
            return real_sum  # ---该函数不返回求和的结果,而是返回求和的函数
        f = lazy_sum(1, 2, 3, 4)  # ---此时函数没有计算结果,而只是生成了对应的函数体
        print("f   is :", f)  # --只打印该函数的地址
        print("f() is :", f())  # --这时才打印该函数的输出
        break


    if part == 4:
        #----------------函数库，模块部分----------------
        print("\n\n----PART4: 模块部分---------------")

        print("\n\n----4.1 系统标准库---------")
        import sys
        print('The command line arguments are:')
        for i in sys.argv:
            print(i)
        print('The PYTHONPATH is（寻找模块的路径）： ', sys.path, '\n')
            #会在输出的path中寻找模块

        print("\n\n----4.2 模块部分:数学模块---------")
        import math

        print("\n\n----4.3 模块部分:操作系统模块---------")
        import os
        path1 = os.getcwd()  # 获取当前目录路径
        print("获取当前目录PATH：",path1)
        ldirs = os.listdir(path1)  # 获取路径中所有文件名字
        print("获取当前目录PATH下的文件: ",ldirs)

        print("\n\n----4.4 模块部分:随机数模块---------")
        import random  # -----模块引用
        for i in range(5):  # -----"range"函数的用法
            a = random.randint(100, 200)
            print(a)

        print("\n\n----4.5 自定模块---------")
        '''《ABOP》创建自己的模块是十分简单的，
        每个 Python 程序也是一个 模块。确保它具有.py 扩展名了即可
        例子：MyMuoKuai.py'''
        import MyMuoKuai
        MyMuoKuai.mod()


        print("\n\n----4.6 第三方函数库---------")
        import MyMuoKuai
        MyMuoKuai.mod()

        break


    if part == 5:
        #----------------Exceptions Handing 错误控制部分----------------
        print("\n\n----Exceptions Handing 部分:未完成---------")

        try:
            #-----在这输入正常的代码
            print("try:正常的代码块部分")
            print(7 / 0)

        except ZeroDivisionError:
            #-----在这输入出现错误(除以0的错误)时的代码
            print("except:出现了错误:除以0的错误")
            pass
        except ImportError:
            pass  # ------pass用来占位,暂时不知道写什么的时候,用pass来代替
        except IndexError:
            pass
        except NameError:
            pass
        except SyntaxError:
            pass
        except TypeError:
            pass
        except ValueError:
            pass
        finally:
            pass
            # file.close()
            #------在文件编程中,final里关闭文件,可以在任何情况避免文件资源占用浪费
        break


    if part == 6:
        #----------------文件编程部分----------------
        print("\n\n----文件创建,打开,写入,关闭,读取---------")

        file1 = open("file.txt", "wr")  # ----w:写.r:读取.b:二进制
        write_num = file1.write("我可以吞下玻璃而不伤身体")  # ---wirte返回值:写入的字符数
        print("write_num is : ", write_num)

        print(file1.read())  # -----read报错!!!!!!!!!!!!!!!!!!!!!!!

        file1.close()  # ----不要忘记close来释放资源,也可以写在try---finally里,保证一定释放

        break


    if part == 7:
        #----------------函数部分----------------
        print("\n\n----函数---------")
        break


    if part == 8:
        print("\n\n----1，简单网络编程：韩寒博客抓取---------")
        '''
        智普教育课程，学习日期：161127
        '''
        #---prthon2
        '''
        import urllib
        url = 'http://www.v2ex.com/'#直接从网页拷贝的
        url_test = urllib.urlopen(url).read()#读取指定url内容
        print url_test
        open('url-test-out','w').write(url_test)#打开并写入
        '''

        
        #---Python3:
        '''
        # Python3的urllib与2很大不同一个是urllib，一个是urllib.request
        import urllib.request
        url = 'http://www.v2ex.com/'
        url_test = urllib.request.urlopen(url).read()

        # 用python3 读取 默认返回的是bytes 而不是 str，所以要用decode解码！
        # 方案1
        url_test_decode = url_test.decode('utf8')
        #print (url_test)
        #print (url_test_decode)
        open('url-test-out2.txt', 'w', encoding='utf-8').write(url_test_decode)
        open('url-test-out2.html', 'w', encoding='utf-8').write(url_test_decode)
        # encoding='utf-8'的由来：在windows下面，新文件的默认编码是gbk
        # python解释器会用gbk编码去解析我们的网络数据流txt
        # 然而txt此时已经是decode过的unicode编码，这样的话就会导致解析不了
        # 解决的办法就是，改变目标文件的编码encoding='utf-8'
        # 方案2
        open('url-test-out.txt', 'wb').write(url_test)
        # 注意：在P3中要用wb！
        '''
        
        print("----------2，Other---------")
        #import webbowser
        # webbowser.open_new_tab("url-test-out2.html")
        import webbrowser
        webbrowser.open("www.baidu.com")

        break


    if part == 9:
        print("\n\n----9: 编码部分---------")
        '''
        Str对象
        	Python的Str对象其实就是8bit-String，字节字符串，类似java的byte【】
        	Python的文件读写的格式
        Unicode对象
        	Python的Unicode对象才等同于java的String对象，类似java的Char【】
        Encode编码
        	使我们看到的直观的字符（unicode）转换成计算机内的字节字符串(str)
        Decode译码
        	把字节数组(str)转换成我们看的懂的、直观的、“人模人样”（unicode）形式
        	转换的方式就是UTF-8
        内置的open函数打开文件时，read方法读取的是一个str(私以为叫做字节数组更合适)
        如果读取的是其它编码的文字，则需要decode之后再做使用。
        '''

        import sys
        #print (sys.getdefaultencoding())
        #查看Python3默认编码格式
        print ('中'.encode('UTF-8'))
        #Unicode型encode编码（UTF-8）成字符串Str
        	#OUT：b'\xe4\xb8\xad'
        print (b'\xe4\xb8\xad'.decode())
        #字符串Str型decode解码（UTF-8）成Unicode型
        	#OUT：中


        break


    if part == 10:
        '''
        171001-http://115.159.189.227/习题解答
        '''

        part1 = input("which part to run  :")
        part1 = float(part1)
        while 1:
            if part1 == 1:
                '''A
                Input
                每行包含两个数a,b (-(2^31)<=a,b<=(2^31)-1)
                Output
                每行一个数，表示a与b的和
                （ACCEPT）已经通过A测试
                '''
                while 1:
                    arr = input("Please input the array：").split(" ")#注意这个split（）
                    #input输入数组arr中，空格做分割
                    print(int(arr[0])+int(arr[1]))#记得转化
                    #求和

            if part1 == 2:
                '''B
                Input
                输入由多组整型的a和b数据构成，a和b数据之间用一个空格隔开，每行只有一对a和b数据，
                当输入的a和b数据都为0时，输入终止。(a,b不会超出int32范围)
                Output
                对于输入的每组不为0的a和b数据，你应该在新的一行输出a与b之和。
                （       ）
                '''
                while 1:
                    arr = [[]]*2000
                    line = 0
                    stopword = '0 0' # 输入停止符
                    str = ''
                    for linein in iter(input, stopword): # 输入为空行，表示输入结束
                            # Py2:raw_input（）。------ Py3:input（）
                        str += linein + '\n' #str为网上拷贝，这里用处不大
                        arr[line] = linein.split(' ')
                        line = line + 1 

                    for line_i in range(line):
                        print (int(arr[line_i][0])+int(arr[line_i][1]))
                    print ('')




            if part1 == 3:
                '''C
                171003-作业
                输入由多组整型数据构成，每组数据在同一行，每行的第一项数据为N，
                表明之后输入的数据有N个，之后的每项数据之间隔一个空格，
                当输入的N为0时，输入终止。(a,b不会超出int32范围)
                171005-ACCEPT-http://115.159.189.227/problem.php?cid=1003&pid=2
                '''
                while 1:
                    arr = [[]]*2000 #这个数组设的很大
                    
                    '''
                    Eg：可以多行输入（包括录入回车）的例子：
                    迭代器的应用
                    修改stopword即可停止。(part1==4，是指定次数的例子)
                    '''
                    stopword = '0' # 输入停止符
                    line = 0 #数组行数
                    str = ''
                    for linein in iter(input, stopword): # 输入为0，表示输入结束
                            # Py2:raw_input（）。------ Py3:input（）
                        str += linein + '\n' #str为网上拷贝，这里用处不大
                        arr[line] = linein.split(' ') #重要！为二维数组arr的每行赋值
                        line = line + 1 #统计输入了几行line，line值也可以用来中断输入循环。
                    
                    '''
                    Eg：二维数组连续求和的例子
                    '''
                    for i in range(line):#求1-line行
                        arr_sum = 0
                        for j in range(1,len(arr[i])):#求该行第2-最后的和
                            arr_sum = arr_sum + int(arr[i][j])
                        print (arr_sum)

                break

            if part1 == 4:
                '''D
                Input
                输入由多个整型数据构成，第一行输入数据N，表明接下来的数据一共有N组。
                接下来的每一行的第一个数据为M，表明每组数据的个数为多少，数据之间用一个空格隔开。(a,b不会超出int32范围)
                Output
                对于输入的每组整数，你应该在新的一行中输出每组除了数据M之外的所有数据的和，
                注意，每个输出之间有一个空白行。
                '''
                
                # 171005-ACCEPT-http://115.159.189.227/problem.php?cid=1003&pid=3

                arr = [[]]*2000
                line = 0
                stopword = '0' # 输入停止符
                stopnum = 100
                str = ''
                for linein in iter(input,stopword): 
                    str += linein + '\n'
                    arr[line] = linein.split(' ')
                    if line == 0:
                        stopnum = int(arr[0][0])+1
                    line = line + 1

                    '''用Stopnum + break 来控制输入行数'''
                    stopnum = stopnum -1
                    if stopnum == 0 :
                        break
                    
                for line_i in range(1,int(line)):
                    arr_sum = 0
                    #计算一行之和
                    for line_j in range(1,len(arr[line_i])): #range从1起，即第一个数不求和
                        arr_sum = int(arr_sum) + int(arr[line_i][line_j])
                    print (arr_sum)

                    #为了配合题目格式，填上空格
                    if line_i < (int(line)-1):
                        print ('')
                break

            if part1 == 6:
                '''
                一个苹果5元钱，一个黑莓3元钱，三份小米一块钱，现在杰哥用自己的一百块钱能买100个食物，苹果，黑莓和小米各多少个。
                Input
                输入一个数据，代表杰哥拥有的钱m。杰哥用m钱买m份食物。
                Output
                多组结果 每行分别输出满足要求的苹果、黑莓、小米的数量，每个元素之间以一个空格间隔。
                Sample Input
                100
                Sample Output
                0 25 75
                4 18 78
                8 11 81
                12 4 84
                '''
                Money = input("Please input the Money：\n")
                Money = int(Money)
                x1 = 0 #苹果
                x2 = 0 #黑莓
                x3 = 0 #小米
                for x1 in range(int(Money/5)): #苹果取值范围
                    for x2 in range(int(Money/3)): #黑莓取值范围
                        for x3 in range(int(Money*3)): #小米取值范围
                            print (x1,' ',x2,' ',x3)
                            if (Money == 5*x1 + 3*x2 + (x3/3)) and ((x1 + x2 + x3) == 100):
                                print (x1,' ',x2,' ',x3)
                        



                break
            if part1 == 7:
                '''
                Input
                有多组输入，每组输入一行，每行一个单词，表示写错的三个单词之一
                已知每个单词最多写错一个字母（不会多写或少写
                Output
                输出这个单词(four five six)对应的数字
                Sample Input
                foor
                fiie
                ssx
                fixe
                Sample Output
                4
                5
                6
                5
                '''
                arr_word_r = [[]]*3
                arr_word_w = [[]]*4
                arr_word_r = [['f', 'o', 'u', 'r','4'],['f', 'i', 'v', 'e','5'],['s', 'i', 'x','','6']]


                #输入四组字符串，每个字母单独存放
                for i in range(4):
                    arr_input = input("Please input the array：")
                    arr_word_w[i] = list(arr_input)#单词拆分成字母
                    print (arr_word_w)

                for w1 in range(4):#检验第1234错误单词
                    for r1 in range(3):#对照第123正确单词
                        sim = 0
                        for w2 in range(len(arr_word_w[w1])):#对照该错误单词第w2位 与 正确单词第w2位
                            #print("\n",arr_word_w[w1],":")
                            if arr_word_w[w1][w2] ==  arr_word_r[r1][w2]:
                                sim = sim + 1
                                #print (w1,w2,r1,w2,arr_word_w[w1][w2],"copy",arr_word_r[r1][w2])
                                if sim == len(arr_word_w[w1]): #字母全对
                                    print("Bingo:",arr_word_r[r1][len(arr_word_r[r1])-1])
                                    break
                                elif sim == (len(arr_word_w[w1])-1): #字母错一个
                                    print("Bingo:",arr_word_r[r1][len(arr_word_r[r1])-1])
                                    break
                break

        break


print ('__MAIN_EXIT__: END loop of Learn')

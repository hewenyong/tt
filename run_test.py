import time
import unittest
from utils.config import REPORT_PATH
from utils.HTMLTestRunner import HTMLTestRunner
from utils.email import SendEmail
if __name__ == '__main__':
    #测试用例目录
    test_dir = 'E:\\pycharm_project\\ui_automation\\test\\case'
    #根据测试目录，查找匹配的测试用例，返回测试套件
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    #获取特定格式的时间
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    #测试报告路径
    report = REPORT_PATH + '//' + now + 'report.html'
    #指定测试报告，运行测试套件
    with open(report, 'wb') as f:
        runner = HTMLTestRunner(f, title='从0搭建测试框架', description='用例执行情况：')
        runner.run(discover)
    #发送邮件
    print(now)
    e = SendEmail()
    e.send_main(report)













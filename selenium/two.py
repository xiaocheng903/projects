import unittest
import HTMLTestRunner
import time
testdir = './testcase'
testreport = './report'
discover = unittest.defaultTestLoader.discover(testdir,pattern='test*.py')
now = time.strftime("%Y-%m-%d %H_%M_%S")
filename = testreport + '/' + now + 'result.html'
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况')
runner.run(discover)








# coding=gbk
"""
    Group Chat Robot v0.1
"""
# coding: utf-8

import itchat, re
from itchat.content import *
import random
import json

"""
    Constants
"""
REPLY = {'����':['�Ҳ�˵��Ĺ�����ô���棬�Ҳ�û�м��������Ǵ���������м䣬�ҷ������ǲ�˹��Ӱ�Ӻ�С������Ϣ�����Ѿ�����һ�ݹ�����ô�򵥣�����һ���������ѣ�',
               '��ӵ�����������ν��������޷�ӵ�е�����ְҵ��̫�����ˣ�',
               '��������£���Ҷ�ϰ��Ϊ����ֻ�����ô�ҿ�ʼ˼��������⣬˵�������ڷ�˼�����ɵ�ǰ���ƶȣ���Ĺ�˾����Ϊ���������˱�ø��ã�'],
         'ѧϰ':['��ô�������ͬ������������һ���ǳ�˼�뽻����ʢ�硣','����Ⱥ���ǵķ��ԣ�������ɽ��������������֮�ƣ�',
               '����仰�����ı�������뱻��ļᶨ�����һ����һ��ִ��׷���Լ�������ˣ�'],
		 'ζ��':['��ֱ���˼���ζ��','�óԵķ���',
               '���������ζ�������ϱ���һ���Ǹ���ʹ��'],
         'default': ['̫����','�治��','�ÿ���','����','ûʲô��˵���ˣ�������һ���ʺ�ƨ��']}

@itchat.msg_register([TEXT], isGroupChat=True)
def text_reply(msg):
#�������Ҹ���һ��*^o^*
    if msg['User']['NickName'] == '�������Ҹ���һ��*^o^*':
        print('Message from: %s' % msg['User']['NickName'])
        # �����ߵ��ǳ�
        username = msg['ActualNickName']
        print('Who sent it: %s' % username)

        match = re.search('����', msg['Text']) or re.search('�Ӱ�', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            print('�������Ӱ� is: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['����']) - 1)
            itchat.send('%s��%s' % (username, REPLY['����'][randomIdx]), msg['FromUserName'])

        match = re.search('ѧϰ', msg['Text']) or re.search('����', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            print('ѧϰ������ is: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['ѧϰ']) - 1)
            itchat.send('%s��%s' % (username, REPLY['ѧϰ'][randomIdx]), msg['FromUserName'])
			
        match = re.search('ζ��', msg['Text']) or re.search('��', msg['Text']) or  re.search('��', msg['Text']) or re.search('��', msg['Text'])
        if match:
            print('-+-+' * 5)
            print('Message content:%s' % msg['Content'])
            print('ζ������ is: %s' % (match is not None))
            randomIdx = random.randint(0, len(REPLY['ζ��']) - 1)
            itchat.send('%s��%s' % (username, REPLY['ζ��'][randomIdx]), msg['FromUserName'])
			
			
			
			
			
        print('isAt is:%s' % msg['isAt'])

        if msg['isAt']:
            randomIdx = random.randint(0, len(REPLY['default']) - 1)
            itchat.send('%s��%s' % (username, REPLY['default'][randomIdx]), msg['FromUserName'])
            print('-+-+'*5)

itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()
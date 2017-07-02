# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/6/30.

def get_old_version():
    handler = open("GameFriendSDKVersion.h", "r")
    content = handler.read()
    handler.close()

    start_length = len("#define GameFriendSDKVersion @\"")
    end_length = len(content) - len("\"")

    return content[start_length:end_length]

def set_new_version(new_version):
    new_string = "#define GameFriendSDKVersion @\"" + new_version + "\""

    handler = open("GameFriendSDKVersion.h", "w")
    handler.write(new_string)
    handler.close()

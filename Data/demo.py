# coding: utf-8 python2
# created by mr.huangjian@foxmail.com on 2017/7/2.

import PersistenceUtil

dict_ = {
    "scoreList": {
        "Chinese":100,
        "Math":100
    }
}

# PersistenceUtil.writePickle("d.pkl", dict_)

print PersistenceUtil.readPickle("d.pkl")

filePath = "temp.json"

# dictContent = {
#     "projectFilePath": "",
#     "versionFilePath": "",
#     "extraInfoFilePath": "",
#     "exportDirPath": "~/Desktop/"
# }

# PersistenceUtil.writeJson(filePath, dictContent)


PersistenceUtil.modifyJson(filePath, "projectFilePath", "not found")



# dictContent = {
#     "projectFilePath": "not found",
#     "versionFilePath": "not found",
#     "extraInfoFilePath": "not found",
#     "exportDirPath": "~/Desktop/"
# }
#
# writeJson(filePath, dictContent)
#
# content = readJson(filePath)
# print type(content)
# print content["exportDirPath"]

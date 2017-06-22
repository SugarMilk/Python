# coding: utf-8
# created by mr.huangjian@foxmail.com on 2017/6/22.

import os

class FileTemplate:

    def __init__(self, class_name):
        self.class_name = class_name
        self.create_api_manager_file_h()
        self.create_api_manager_file_m()

    def create_api_manager_file_h(self):
        content_h = """\
//
//  %s.h
//

#import "%s.h"

@interface %s : GFAPIBaseManager <GFAPIManager, GFAPIManagerValidator>

@end
        """ % (self.class_name, self.class_name, self.class_name)

        io = open(os.environ['HOME'] + "/Desktop/" + self.class_name + ".h", "wb")
        io.write(content_h);
        io.close()

    def create_api_manager_file_m(self):
        content_m = """\
//
//  %s.m
//

#import "%s.h"

@interface %s ()

@property (nonatomic, copy) NSString * methodName;
@property (nonatomic, copy) NSString * serviceType;
@property (nonatomic, assign) GFAPIManagerRequestType requestType;

@end

@implementation %s

- (instancetype)init {
    if (self = [super init]) {
        self.methodName = @"<#MethodName#>";
        self.requestType = GFAPIManagerRequestTypePost;
        self.serviceType = kGFServiceSdk;
        self.validator = self;
    }
    return self;
}

#pragma mark - GFAPIManager

- (NSDictionary *)reformParams:(NSDictionary *)params {
    NSMutableDictionary * allParams = [NSMutableDictionary dictionaryWithDictionary:params];
    return allParams;
}

#pragma mark - GFAPIManagerValidator

- (BOOL)manager:(GFAPIBaseManager *)manager isCorrectWithParamsData:(NSDictionary *)data {
    return YES;
}

- (BOOL)manager:(GFAPIBaseManager *)manager isCorrectWithCallBackData:(NSDictionary *)data {
    return YES;
}

@end
        """ % (self.class_name, self.class_name, self.class_name, self.class_name)

        io = open(os.environ['HOME'] + "/Desktop/" + self.class_name + ".m", "wb")
        io.write(content_m);
        io.close()
        pass


FileTemplate("GFAutoLoginAPIManager")
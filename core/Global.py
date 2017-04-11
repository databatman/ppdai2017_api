#coding=utf-8
__author__ = "yangl"
'''''
全局变量
'''
'''''
publickey为服务端的公钥
privatekey为自己客户端的私钥
PS：python的密钥都是PKCS1的
站点上的客户端私钥需要剔除
-----BEGIN RSA PRIVATE KEY-----
AND
-----END RSA PRIVATE KEY-----
并且将回车符剔除
'''

# https://ac.ppdai.com/oauth2/smslogin?AppID=566c28d1aad64ed19a46b9f4d6d99ed4&ReturnUrl=http%3A%2F%2Fwww.ppdai.com


privatekey='-----BEGIN RSA PRIVATE KEY-----\nMIICXAIBAAKBgQCSsVhqzlIb1K5HvDUh0vFimQ1rMQFhEXk78nPRG+Nrjd8UJ+k73hgzASG0IQ30vLAb8G9pB7glJpfzhrkwqQlp72tQWyQ3rIjKzgSEMwbIrfUS0uYw6jTDRaioPkDjIcVvdeDrg6jqzgCopXWVsyg/+scy8WuMiawG6g19BVJHbwIDAQABAoGAM9N4O3PdSnvffvSdiO+v3HfaZ86OgC7eODG2fWBu/qbG86YOHtqejhaOQ8eR2K95QMW3dtIFWwrBkIY+k1SFQF3mcMXknC7+6niC82Xz8q3DJEP++l5FukPfzGDFWeWwsDlRsP0f4VYhskXGKhrGfcr3ztPddaL/YtPHOHolKgECQQDw9ge1Z6ejGYbRXRuvc28Ie6hhNlO0q18cfqajAFfJlpOVUUJKZmgXBEUNt9E263ZJeJ2P6vV+iX978q+zS7WBAkEAm9kjRegOxQy29S+rG5YVzrd2yuX+Ar4Ug83FXWfU1f+a0jumq/MINa5N4kGxooIVR7kDxYmYbnn3Cu2fa9XU7wJAS/9tAvwEVV6xtMrG9plTxbsqqi52TB9YyiXv7K0pAv2o4olUfR67abcBCIiXRdkR365ZE5EpiJVZTgCHBee1AQJBAJR4uYzoteFt6oMNJaLDSgVEbSyBDYvJUDv89dC1kWNJ/lHYuEFJ6AFUDCjH0xXxfZp1nS08l3ZwRTUpCd6uuQsCQH4tzMOaaSpQUCxS2ZLQ9flZodiE4rrCqGE8yEUZ0/MC7uiglrCkFH6RsPACL2UmAGx9YArr7Q3nxUEgo+hpSuE=\n-----END RSA PRIVATE KEY-----'

publickey='-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCSsVhqzlIb1K5HvDUh0vFimQ1rMQFhEXk78nPRG+Nrjd8UJ+k73hgzASG0IQ30vLAb8G9pB7glJpfzhrkwqQlp72tQWyQ3rIjKzgSEMwbIrfUS0uYw6jTDRaioPkDjIcVvdeDrg6jqzgCopXWVsyg/+scy8WuMiawG6g19BVJHbwIDAQAB\n-----END PUBLIC KEY-----'

# 一次性
code="3f5b6464a9a643d3849bc6851080475f"

AppId="566c28d1aad64ed19a46b9f4d6d99ed4"

OpenID="e3aa0536409044f8a035ba2a73d2c4c7"

AccessToken = "dd537d68-3945-4e27-b0d7-ca5b2cca5842"

RefreshToken= "3780d739-1029-42a6-a30a-c56aef5b3fab"
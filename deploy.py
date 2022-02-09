from brownie import accounts

def deploy_simple_storage():
    account = accounts[0]
    print(account)

def main():
    print('hello')
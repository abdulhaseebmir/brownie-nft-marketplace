from brownie import accounts, BasicNft

def deploy_basic_nft():
    account = accounts[0]
    print("Deploying Basic Nft...")
    basic_nft = BasicNft.deploy({
        "from": account
    })
    print(f"Deployed Basic Nft at: {basic_nft.address}")

def main():
    deploy_basic_nft()
    account = accounts[0]
    account = accounts[0]

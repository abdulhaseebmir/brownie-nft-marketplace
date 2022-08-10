from brownie import accounts, BasicNft
from scripts.helpful_scripts import get_account

def deploy_basic_nft():
    account = get_account()
    print("Deploying Basic Nft...")
    basic_nft = BasicNft.deploy({
        "from": account
    }, publish_source=True)
    print(f"Deployed Basic Nft at: {basic_nft.address}")

def main():
    deploy_basic_nft()

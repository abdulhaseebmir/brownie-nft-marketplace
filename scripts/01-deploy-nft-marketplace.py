from brownie import accounts, NftMarketplace
from scripts.helpful_scripts import get_account

def deploy_nft_marketplace():
    account = get_account()
    print("Deploying NftMarketplace...")
    nft_marketplace = NftMarketplace.deploy({
        "from": account
    })
    print(f"Deployed NftMarketplace at: {nft_marketplace.address}")


def main():
    deploy_nft_marketplace()
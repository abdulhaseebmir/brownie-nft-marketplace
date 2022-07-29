from brownie import accounts, NftMarketplace

def deploy_nft_marketplace():
    account = accounts[0]
    print("Deploying NftMarketplace...")
    nft_marketplace = NftMarketplace.deploy({
        "from": account
    })
    print(f"Deployed NftMarketplace at: {nft_marketplace.address}")


def main():
    deploy_nft_marketplace()
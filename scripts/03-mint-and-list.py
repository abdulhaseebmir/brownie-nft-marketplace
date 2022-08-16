from brownie import NftMarketplace, BasicNft, accounts
from web3 import Web3
from scripts.helpful_scripts import get_account

PRICE = Web3.toWei("0.1", "ether")

def mint_and_list():
    account = get_account()
    basic_nft = BasicNft[-1]
    nft_marketplace = NftMarketplace[-1]
    
    # account = get_account()
    # nft_marketplace = NftMarketplace.deploy({
    #     "from": account
    # })
    # basic_nft = BasicNft.deploy({
    #     "from": account
    # })
    print("Minting...")
    mint_tx_receipt = basic_nft.mintNft({"from": account})
    mint_tx_receipt.wait(1)
    token_id = mint_tx_receipt.events[0]["tokenId"]
    print(f"Basic NFT of token ID: {token_id} minted!")
    
    print("Approving NFT...")
    approval_tx = basic_nft.approve(nft_marketplace.address, token_id, {"from": account})
    approval_tx.wait(1)

    print("Listing NFT...")
    market_place_tx = nft_marketplace.listItem(basic_nft.address, token_id, PRICE, {"from": account})
    market_place_tx.wait(1)
    print("Listed!")


def main():
    mint_and_list()
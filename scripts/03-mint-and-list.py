from brownie import NftMarketplace, BasicNft, accounts
from web3 import Web3

PRICE = Web3.toWei("0.1", "ether")

def mint_and_list():
    nft_marketplace = NftMarketplace.deploy({
        "from": accounts[0]
    })
    basic_nft = BasicNft.deploy({
        "from": accounts[0]
    })
    print("Minting...")
    mint_tx_receipt = basic_nft.mintNft()
    mint_tx_receipt.wait(1)
    token_id = mint_tx_receipt.events[0]["tokenId"]
    print(f"Basic NFT of token ID: {token_id} minted!")
    
    print("Approving NFT...")
    approval_tx = basic_nft.approve(nft_marketplace.address, token_id)
    approval_tx.wait(1)

    print("Listing NFT...")
    market_place_tx = nft_marketplace.listItem(basic_nft.address, token_id, PRICE)
    market_place_tx.wait(1)
    print("Listed!")


def main():
    mint_and_list()
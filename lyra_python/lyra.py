import web3
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account.account import Account
from eth_account.signers.local import LocalAccount

# TODO: add typing to all functions


class Lyra:
    def __init__(self, network=None, w3=None, private_key=None):
        pass
        # TODO: if network is not None, set self.network to network
        # if w3 is not None, set self.w3 to w3 and parse network from w3
        # if both are None, raise an error
        # if w3 is None and network is not None, set self.w3 to w3 with standard API
        # if private_key is not None, set LocalAccount from private key

    def set_up(self):
        pass
        # TODO: set up Lyra contracts

    # Functionalities to add

    # - Getting Live boards.
    # - Getting option prices.
    # - Executing trades.
    # - Deposit/Withdraw to vaults.
    # - GetMinCollateral
    # - GetLiquidationPrice

    #############################
    ########  Getters   #########
    #############################
    def get_live_boards(self):
        pass

    def getLiveBoards(self):
        return self.get_live_boards()

    def get_option_price(self, market, strike, expiry, option_type, amount=1):
        pass

    def getOptionPrice(self, market, strike, expiry, option_type, amount=1):
        return self.get_option_price(market, strike, expiry, option_type, amount)

    def get_option_prices(self, market, strike, expiry, option_type, amount=1):
        pass

    def getOptionPricse(self, market, strike, expiry, amount=1):
        return self.get_option_price(market, strike, expiry, amount)

    def get_min_collateral(self, market, strike, expiry, option_type, amount):
        pass

    def getMinCollateral(self, market, strike, expiry, option_type, amount):
        return self.get_min_collateral(market, strike, expiry, option_type, amount)

    def get_liquidation_price(self, market, strike, expiry, option_type, amount):
        pass

    def getLiquidationPrice(self, market, strike, expiry, option_type, amount):
        return self.get_liquidation_price(market, strike, expiry, option_type, amount)

    #############################
    ########  Trading   #########
    #############################
    def execute_trade(self, trade_params, is_close=False):
        pass

    def executeTrade(self, trade_params, is_close=False):
        return self.execute_trade(trade_params, is_close)

    #############################
    ####  Deposit/Withdraw   ####
    #############################
    def deposit(self, market, amount):
        pass

    def withdraw(self, market, amount):
        pass

    #############################
    ########  Utilities   #######
    #############################
    # TODO: put inside a utils.py file

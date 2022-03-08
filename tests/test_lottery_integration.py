from brownie import Lottery, config, network,accounts
import pytest
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, fund_with_link, get_account, fund_with_link
from scripts.deploy_lottery import deploy_lottery
import time

def test_can_pick_winner():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    lottery = deploy_lottery()
    account = get_account()
    lottery.startLottery({"from":account})
    lottery.enter({"from":account, "value": lottery.getEntranceFee()})
    lottery.enter({"from":account, "value": lottery.getEntranceFee()})
    fund_with_link(lottery)
    lottery.endLottery({"from":account})
    # does not need to pretend as chainlink node as it real network
    time.sleep(60)
    assert lottery.recentWinner() == account
    assert lottery.balance() == 0
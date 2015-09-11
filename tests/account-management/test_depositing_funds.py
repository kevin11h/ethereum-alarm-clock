from populus.utils import wait_for_transaction


deploy_max_wait = 15
deploy_max_first_block_wait = 180
deploy_wait_for_block = 1

geth_max_wait = 45


def test_depositing_funds(geth_node, geth_coinbase, deployed_contracts):
    alarm = deployed_contracts.Alarm

    assert alarm.accountBalances.call(geth_coinbase) == 0

    txn_1_hash = alarm.deposit.sendTransaction(geth_coinbase, value=123)
    wait_for_transaction(alarm._meta.rpc_client, txn_1_hash)

    assert alarm.accountBalances.call(geth_coinbase) == 123

    txn_2_hash = alarm.deposit.sendTransaction(geth_coinbase, value=456)
    wait_for_transaction(alarm._meta.rpc_client, txn_2_hash)

    assert alarm.accountBalances.call(geth_coinbase) == 579

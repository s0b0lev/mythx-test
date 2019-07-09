#!/usr/bin/env python
import logging
import time

from pythx import Client


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

# SWC-100 visibility_not_set.sol
API_PAYLOAD = {
    "contract_name": "HashForEther",
    "bytecode": "608060405234801561001057600080fd5b5061011d806100206000396000f3006080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806383ac4ae114604e578063cc42e83a146062575b600080fd5b348015605957600080fd5b5060606076565b005b348015606d57600080fd5b50607460d5565b005b3373ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f1935050505015801560d2573d6000803e3d6000fd5b50565b60003363ffffffff1614151560e957600080fd5b60ef6076565b5600a165627a7a72305820b27fdb0b720929ae434b4424a0a4baefc1f0360ae870d73ef4fec622b9a863960029",
    "source_map": "158:288:0:-;;;;8:9:-1;5:2;;;30:1;27;20:12;5:2;158:288:0;;;;;;;",
    "deployed_bytecode": "6080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806383ac4ae114604e578063cc42e83a146062575b600080fd5b348015605957600080fd5b5060606076565b005b348015606d57600080fd5b50607460d5565b005b3373ffffffffffffffffffffffffffffffffffffffff166108fc3073ffffffffffffffffffffffffffffffffffffffff16319081150290604051600060405180830381858888f1935050505015801560d2573d6000803e3d6000fd5b50565b60003363ffffffff1614151560e957600080fd5b60ef6076565b5600a165627a7a72305820b27fdb0b720929ae434b4424a0a4baefc1f0360ae870d73ef4fec622b9a863960029",
    "deployed_source_map": "158:288:0:-;;;;;;;;;;;;;;;;;;;;;;;;;;;;;367:77;;8:9:-1;5:2;;;30:1;27;20:12;5:2;367:77:0;;;;;;187:173;;8:9:-1;5:2;;;30:1;27;20:12;5:2;187:173:0;;;;;;367:77;403:10;:19;;:33;423:4;:12;;;403:33;;;;;;;;;;;;;;;;;;;;;;;;8:9:-1;5:2;;;45:16;42:1;39;24:38;77:16;74:1;67:27;5:2;403:33:0;367:77::o;187:173::-;325:1;310:10;303:23;;;295:32;;;;;;;;337:15;:13;:15::i;:::-;187:173::o",
    "main_source": "visibility_not_set.sol",
    "sources": {
        "visibility_not_set.sol": {
            "source": "/*\n * @source: https://github.com/sigp/solidity-security-blog#visibility\n * @author: SigmaPrime \n * Modified by Gerhard Wagner\n */\n\npragma solidity ^0.4.24;\n\ncontract HashForEther {\n\n    function withdrawWinnings() {\n        // Winner if the last 8 hex characters of the address are 0. \n        require(uint32(msg.sender) == 0);\n        _sendWinnings();\n     }\n\n     function _sendWinnings() {\n         msg.sender.transfer(this.balance);\n     }\n}\n"
        }
    },
    "source_list": ["visibility_not_set.sol"],
    "analysis_mode": "quick",
}


def main():
    c = Client(
        eth_address="0x0000000000000000000000000000000000000000", password="trial"
    )
    logging.debug("Submit analysis to API")
    resp = c.analyze(**API_PAYLOAD)

    while not c.analysis_ready(resp.uuid):
        logging.debug("Checking analysis status")
        time.sleep(1)

    return c.report(resp.uuid)


if __name__ == "__main__":
    logging.debug("Running MythX API tests")
    main()

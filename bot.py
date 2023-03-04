import os
import discord
from web3 import Web3
from eth_account import Account

# Connect to the Ethereum network using Infura
w3 = Web3(Web3.HTTPProvider(os.environ['INFURA_URL']))

# Define contract address and ABI
contract_address = '0x...'
contract_abi = [...]
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# Define Discord bot client
client = discord.Client()

# Define event listener function
def handle_event(event):
    # Get Discord channel object for the desired channel
    channel = client.get_channel(channel_id)

    # Send message to Discord channel
    message = f"A mint has taken place on the smart contract! TxHash: {event['transactionHash'].hex()}"
    channel.send(message)

# Set up Discord bot event listener
@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # Subscribe to smart contract events
    contract_event_filter = contract.events.Mint.createFilter(fromBlock='latest')
    while True:
        for event in contract_event_filter.get_new_entries():
            handle_event(event)

# Start Discord bot
client.run(os.environ['DISCORD_BOT_TOKEN'])

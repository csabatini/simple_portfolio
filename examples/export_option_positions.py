from simple_portfolio import fetch, export
import configparser

config = configparser.ConfigParser()
config.read('config.debug.ini')
account = dict(
        username= config['account']['username'],
        password= config['account']['password']
)


fetch_options = {}
positions = fetch.option_positions(account, fetch_options)
print("Fetched {} positions".format(len(positions)))


fn = "option_positions.csv"
export_options = { "filename": fn }

export.option_positions(positions, export_options)
print("Finished writing positions to {}".format(fn))

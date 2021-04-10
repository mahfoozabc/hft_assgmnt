from src.obook import Orderbk

'''
Basic liquidity ethics
'''

bk = Orderbk()

# 0 0 0
print(bk.ask_size, bk.bid_size, bk.total_volume_traded)

# LMT sell 10pcs @12.5
bk.submit_order('lmt', 'ask', 10, 12.5, 1)

# LMT buy 10pcs @10.5
bk.submit_order('lmt', 'bid', 10, 10.5, 2)

# 10 10 0
print(bk.ask_size, bk.bid_size, bk.total_volume_traded)

# Satisfies market demand on both sides
bk.submit_order('lmt', 'bid', 10, 20, 3)
bk.submit_order('lmt', 'ask', 10, 5, 3)

# 0 0 20
print(bk.ask_size, bk.bid_size, bk.total_volume_traded)

'''
Market microstructure
---
Implementation is not making concrete orders public
only order sizes on given level
'''

bk = Orderbk()

# Get 5 levels of order bk
# [[], []]
print(bk.get_mkt_depth(5))

bk.submit_order('lmt', 'ask', 2, 10, 1)
bk.submit_order('lmt', 'ask', 4, 20, 1)
bk.submit_order('lmt', 'ask', 6, 30, 1)

bk.submit_order('lmt', 'bid', 1, 1, 2)
bk.submit_order('lmt', 'bid', 5, 2, 2)
bk.submit_order('lmt', 'bid', 7, 3, 2)

# [[[Price, Size] * n], [[Price, Size] * n]]
print(bk.get_mkt_depth(3))

# ([IDs], [{ID: (size, side, priority_id)}])
# Orderbk respects time priority. It means that if
#  trader A submitted LMT buy @10 and trader B did same
#  then trader A is traded first
print(bk.get_participant_orders(1))
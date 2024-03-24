# Wheel                          Segment                           Reward
# -----                          --------                          ------
# - segments: List[Segment]      - reward: Reward                  - name: str
# - spin(): Segment              - index: int                      - value: Any
# + add_segment(segment: Segment) - get_reward(): Reward
# + remove_segment(index: int)
# Wheel
# 属性：segments 是一个 Segment 对象的列表。
# 方法:
# spin()：执行旋转动作，随机选中一个 Segment 并返回它。
# add_segment(segment: Segment)：向转盘添加一个新的分段。
# remove_segment(index: int)：移除一个指定索引的分段。
# Segment
# 属性：
# reward：一个 Reward 对象，表示分段中的奖励。
# index: 表示分段在转盘中的位置。
# 方法：
# get_reward()：返回该分段的奖励。
# Reward
# 属性：
# name：奖励的名称。
# value：奖励的具体内容或值。

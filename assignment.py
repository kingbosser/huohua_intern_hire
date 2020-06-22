from adapter import StreamAdapter
from typing import Dict, Hashable, Iterable
import json


class CourseWareB(StreamAdapter):

	@classmethod
	def load_state(cls, raw_state: str) -> Hashable:
		state = json.loads(raw_state).get("commonComponentState")
		panel_state = (0, 0, 0, 0)
		if state is not None:
			if "4cb5f12f9e164c6c545a55202bc818f2" in state:
			    panel_state = tuple(state["4cb5f12f9e164c6c545a55202bc818f2"]["answer"])
		return panel_state

	@classmethod
	def right_ans(cls, stream: Iterable) -> bool:
		right_ans = (1, 2, 0, 3)
		return tuple(stream) == right_ans

"""
在下面定义CourseWareB
答案状态在commonComponentState下的4cb5f12f9e164c6c545a55202bc818f2下的answer字段
正确答案是1，2，0，3
"""

if __name__ == "__main__":
	"""
	在这里处理日志输出，输出结果为result.csv，三个字段为：学生ID，状态，是否为正确状态
	"""
	
	# 读取data.csv
	f = open("./data.csv",encoding="utf-8")
	lines = f.readlines()
	# 结果文件内容拼接
	string = "uid" + "\t" + "state" + "\t" + "is_right" + "\n"
	# 正确答案
	right_answer = [1, 2, 0, 3]
	for i in range(len(lines)):
		# 跳过第一行表头
		if i == 0:
			pass
		else:
			# 获取每一个字段
			arr = lines[i].split("\t")
			uid = arr[0]
			cr_code = arr[1]
			trace_id = arr[2]
			state = arr[3]
			ctime_ts = arr[4]
			# 处理state字段
			currentstate = json.loads(state).get("commonComponentState")["4cb5f12f9e164c6c545a55202bc818f2"]["answer"]
			is_right = currentstate == right_answer
			# 拼接内容
			string += str(uid) + "\t" + str(currentstate) + "\t" + str(is_right) + "\n"
	f.close()
	# 写文件
	fw = open("./result.csv","w",encoding="utf-8")
	fw.write(string)
	fw.close()
	
			


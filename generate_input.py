import json
import random


data = {
 "operand_stack": [
   "10000",
   "20000"
 ],
 "advice_stack": ["0"]
}


for i in range(10000):
    operation = random.choice(["1", "2", "3", "4"])
    data["operand_stack"].insert(0, operation)
    data["operand_stack"].insert(0, "10")

with open("input_generated.json", "w") as f:
    json.dump(data, f)

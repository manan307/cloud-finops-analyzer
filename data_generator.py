import pandas as pd
import random
def generate_cloud_data():
    services = ["EC2","S3","RDS","Lambda"]
    data = []
    for i in range(10):
        service = random.choice(services)
        resource = service + "-" + str(random.randint(100,999))
        cost = random.randint(20,500)
        cpu = random.randint(0,100)
        day = random.randint(1,5)
        data.append([service,resource,cost,cpu,day])
    df = pd.DataFrame(data, columns=["service","resource_id","cost","cpu_usage","day"])
    df.to_csv("data/cloud_cost.csv", index=False)
import time

import requests


def send_ply_post(path):
    # Define the URL
    url = 'http://127.0.0.1:8080'

    # Define the data to be sent
    data = path


    # Send the POST request with JSON data
    response = requests.post(url, json=data)

    # Print the response from the server (optional)
    print(response.text)


if __name__ == '__main__':
    send_ply_post("C:/Users/Chris/gaussian-splatting/output/d1194e54-c/point_cloud/iteration_11000/point_cloud.ply"
                  )
    #iters= [1, 51, 101, 151, 201, 251, 301, 351, 401, 451, 500, 600, 700, 800, 900, 1000, 1000,
    #                             1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3800,
    #                             4000, 4200, 4400, 4600, 4800, 5000, 5200, 5400, 5600, 5800, 6000, 6200, 6400, 6600,
    #                             6800, 7000, 7200, 7400, 7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400,
    #                             9600, 9800, 10000, 10000, 10500, 11000, 11500, 12000, 12500, 13000, 13500, 14000,
    #                             14500, 15000, 15500, 16000, 16500, 17000, 17500, 18000, 18500, 19000, 19500, 20000,
    #                             20500, 21000, 21500, 22000, 22500, 23000, 23500, 24000, 24500, 25000, 25500, 26000,
    #                             26500, 27000, 27500, 28000, 28500, 29000, 29500, 30000]
    #for iteration in iters:
    #    time.sleep(2)



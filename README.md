Three components - Sensors; Gateway; Cloud
Each component is hosted with a docker container

Through the network, sensor sends information to Gateway, while gateway sends information to cloud server

This Project is about easing out the traffic congestion when soars of data is sent between the sensor and gateway, and between the gateway and sensor. This is achieved by removing redundant data from the send queue, and also remove the regular data which is usually sent between the servers.

Regular data is perceived by application of a moving average with a forgetting factor of 20%

When the time taken for a particular data sample to be sent is more than a set threshold, we end up allocating more resources than actual, which helps in quicker processing, and vice versa when falls below the set threshold. This way the resource allocation for the server is reduced and helps in easing out the traffic when more resources needs to flow through.

We have three applications running at the same time(sensor(multiple), gateway and cloud). We also maintain docker stats with artillery framework running at the same time to measure the statistics

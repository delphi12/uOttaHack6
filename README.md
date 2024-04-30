# uOttaHack6
University of Ottawa Hackathon 

Problem statement: Create any application using solace's products - solace cloud, pub/sub etc.

Title 
Industrial IoT for Predictive Maintenance 

 => using solace cloud and Pub/sub architecture
 
Components: Sensors (Humidity, LDR, temperature, ultrasonic), IoT gateways, cloud-based predictive analytics platform.
Functionality: Manufacturers can monitor the condition of their industrial equipment in real-time using IoT sensors. By analyzing data on equipment performance, LDR patterns, temperature fluctuations, and other factors, they can predict when maintenance is needed to prevent costly breakdowns and optimize production uptime.

We used Arduno UNO to collect data from various sensors (LDR, Humidity, Temperature and Ultrasonic) and sent them to solace cloud through python socket programming. The Data is then monitered in solace using their dashboard. We also connected solace with AWS s3 bucket storage 

# sensor-evaluation
Sensor Evaluation Application
This Python application automates the processing and quality control evaluation of sensor log files. It uses data from thermometers and humidity sensors to classify the devices based on specific evaluation criteria.

Prerequisites
Docker
Kubernetes
Helm
Python 3.8 (for local testing)

Application Setup
Clone the repository:
git clone https://github.com/marysoniaugokwe/sensor-evaluation.git
cd sensor_evaluation
Install Python dependencies:

pip install -r requirements.txt
Run the script locally:

python3 sensor_evaluation.py sensor_data.log results.json
Dockerization and Deployment
Build the Docker image:

docker build -t dockerhubusername/sensor-evaluation .
Run the Docker image:

docker run -p 5000:5000 dockerhubusername/sensor-evaluation
Push the Docker image to Docker Hub:

docker push dockerhubusername/sensor-evaluation
Deploy the application to Kubernetes with Helm:

Modify the image repository and tag in the values.yaml file to match your Docker Hub repository and tag.

Deploy the Helm chart:
helm install sensor-evaluation ./sensor-evaluation-chart
To access the application within the Kubernetes cluster, port-forward the service to your local machine:

export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=sensor-evaluation,app.kubernetes.io/instance=sensor-evaluation" -o jsonpath="{.items[0].metadata.name}")
export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
kubectl --namespace default port-forward $POD_NAME 5000:$CONTAINER_PORT
You can then access the application at http://localhost:5000.

## Monitoring and Logs

Our application uses various metrics and logs to ensure optimal performance and facilitate troubleshooting. Here are some of the key metrics and logs we focus on:

### Application Performance Metrics

- **Latency:** Measures the time it takes to process a log file.
- **Throughput:** Indicates the number of log files that can be processed per unit of time.
- **Error Rate:** Tracks how often errors occur during the processing of log files.

### Resource Usage Metrics

- **CPU Usage:** Tracks the amount of CPU resources the application is using.
- **Memory Usage:** Monitors the amount of memory the application is consuming.
- **Disk I/O:** Tracks how much data is being read from or written to the disk.

### Application-Specific Logs

- **Processing Logs:** Provide information about the processing of each file, such as start time, end time, number of sensors processed, classification results, and any errors or exceptions encountered.
- **Debug Logs:** More detailed logs that can help diagnose problems or understand the application's behavior.

### System Logs

- **Docker Logs:** Logs produced by the Docker daemon, providing information about the container's operation.
- **Kubernetes Logs:** Logs produced by Kubernetes, providing information about the scheduling and management of your application's pods.

## Alerts

Our application includes a comprehensive alerting system that warns us of potential performance issues or infrastructure problems. Here are some of the potential alerts:

### Application Performance Alerts

- **High Error Rate:** An alert is triggered if the error rate of our application exceeds a predefined limit. This can help identify potential issues in the code, input data anomalies, or underlying infrastructure problems.

- **High Latency:** We have configured alerts for sudden spikes in application latency. If the processing time for our logs significantly increases, it could indicate performance bottlenecks that need to be addressed.

- **Low Throughput:** Alerts will be triggered if the number of log files processed per unit of time drops significantly. This could be an indication that our application may not be able to handle the incoming load efficiently.

### Resource Usage Alerts

- **High CPU Usage:** Alerts will be triggered if the CPU usage exceeds a predefined limit. High CPU usage can signal inefficient code or excessive application load that could degrade performance.

- **High Memory Usage:** Alerts will be triggered if memory usage goes beyond a specified limit. High memory usage could indicate a potential memory leak or that the application needs more resources than what's currently allocated.

## CI/CD Recommendation

For Continuous Integration (CI) and Continuous Deployment (CD), we recommend using GitHub Actions. Given that our application code is hosted on GitHub, GitHub Actions provides a seamless and convenient approach to automating software workflows. It provides an end-to-end pipeline right within your repository.

GitHub Actions enable you to:

- Automate your workflow from idea to production
- Implement CI/CD capabilities directly from your repository
- Build, test, and deploy your code right from GitHub
- Deploy updates to Kubernetes

### How to Set Up a GitHub Action Workflow for CI/CD

1. Go to your GitHub repository, click on the 'Actions' tab.
2. Click on 'New Workflow'.
3. Choose to set up a workflow yourself or choose from the existing templates.
4. Write your workflow in YAML format, defining steps that leverage GitHub Actions' vast library of community-created actions.
5. Commit your changes to the repository. The workflow will trigger as configured, usually on a code push or a pull request.

A basic CI/CD workflow should include steps to build the Docker image, push it to a Docker registry, and update the Kubernetes deployment.










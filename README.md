# Deep Reinforcement Learning for Intrusion Detection and Prevention System (IDPS) in IoT Devices

This repository presents an Intrusion Detection and Prevention System (IDPS) designed for IoT devices, utilizing Machine Learning (ML) and Deep Reinforcement Learning (DRL). The system detects and classifies attacks on IoT networks and proactively mitigates threats with a reinforcement learning-based prevention mechanism.

## Features

- **Device Classification**: Classifies IoT devices using a [Random Forest (RF)](https://en.wikipedia.org/wiki/Random_forest) algorithm.
- **Attack Detection**: Detects intrusions using a [Convolutional Neural Network (CNN)](https://en.wikipedia.org/wiki/Convolutional_neural_network).
- **Attack Identification**: Identifies attack types via the [XGBoost](https://xgboost.ai/) model.
- **Proactive Threat Mitigation**: Utilizes [Deep Deterministic Policy Gradient (DDPG)](https://spinningup.openai.com/en/latest/algorithms/ddpg.html) reinforcement learning to mitigate attacks.

## Technologies Used

- Python
- Machine Learning ([Random Forest](https://en.wikipedia.org/wiki/Random_forest), [CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network), [XGBoost](https://xgboost.ai/))
- Deep Reinforcement Learning ([DDPG](https://spinningup.openai.com/en/latest/algorithms/ddpg.html))
- Autoencoders for synthetic data generation

## Installation
1. Clone the repository:
 ```bash
   git clone https://github.com/yourusername/IDPS-IoT.git
 
  ```
2. Navigate to the project directory:
   ```bash
   cd IDPS-IoT
   ```
3.  Install the required dependencies:
  ```bash
  pip install -r requirements.txt
  ```

## Code

### Machine Learning Pipeline

The machine learning pipeline involves classifying IoT devices, detecting attacks, and identifying attack types. The pipeline is designed with four stages:

1. **Device Identification**: Uses Random Forest to classify IoT devices.
2. **Attack Detection**: A CNN detects whether the device is under attack.
3. **Attack Type Identification**: XGBoost identifies the type of attack if detected.
4. **Proactive Defense**: A Deep Deterministic Policy Gradient (DDPG) algorithm mitigates attacks.

### Reinforcement Learning

The **Reinforcement Learning (RL)** agent is trained using the Deep Deterministic Policy Gradient (DDPG) to provide corrective actions for the IoT devices under attack. The RL agent ensures proactive defense by adjusting mitigation strategies based on the type of attack.

The RL agent's key functions:

- **State**: Represents the IoT device's features and the environment state.
- **Action**: Mitigation strategies such as packet dropping or traffic filtering.
- **Reward**: A score based on how well the agent mitigates the attack while minimizing false positives and system disruptions.

### The code structure includes:

- **`run_detection.py`**: For detecting and classifying IoT devices and attacks.
- **`run_prevention.py`**: For mitigating detected attacks using RL.


## Usage

### Running the Detection System

1. Prepare the IoT Dataset (e.g., [BoT-IoT dataset](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/)).
2. Preprocess the dataset using the provided scripts and load it into the system.
3. Run the device classification and attack detection system using:
   ```bash
   python run_detection.py
   ```
This will classify devices and detect attacks on your IoT network.

### Running the Prevention System

After attack detection, the prevention system is executed to mitigate attacks using the trained RL model.

Run the prevention mechanism to dynamically respond to threats:

```bash
python run_prevention.py
```
This will engage the reinforcement learning agent to issue corrective actions and prevent attacks such as DDoS or ransomware.

## Dataset

The [BoT-IoT dataset](https://www.unsw.adfa.edu.au/unsw-canberra-cyber/cybersecurity/ADFA-NB15-Datasets/) is used for training and evaluation. Ensure you have the dataset ready before running the pipeline.

## Methodology

The IDPS follows a structured four-phase ML pipeline for IoT security:

1. **Device Identification**: IoT devices are classified using a Random Forest (RF) algorithm.
2. **Attack Detection**: A Convolutional Neural Network (CNN) analyzes device data to detect attacks.
3. **Attack Type Identification**: If an attack is detected, the XGBoost model identifies the type of attack.
4. **Proactive Mitigation**: The Deep Deterministic Policy Gradient (DDPG) algorithm is used to mitigate attacks, providing corrective actions for affected IoT devices.

### Reinforcement Learning

The system leverages Deep Deterministic Policy Gradient (DDPG) reinforcement learning for proactive defense. The RL agent responds to detected attacks and applies appropriate corrective measures, improving the overall resilience of the IoT ecosystem.

## Evaluation

Our system was tested using the BoT-IoT dataset. The evaluation demonstrated high performance in detecting and mitigating DDoS and ransomware attacks on various IoT devices, including:

- **Precision and Recall** metrics for the attack detection model.
- **Confusion Matrix** to visualize the classification performance.
- **Reward Metrics** from the reinforcement learning agent.

## [Results](./RL_IDPS.pdf)

- **Device Identification**: Accurate classification of IoT devices using Random Forest.
- **Attack Detection**: The CNN achieved high accuracy in detecting network attacks.
- **Attack Type Identification**: XGBoost successfully classified attack types.
- **Proactive Defense**: The DDPG agent effectively mitigated DDoS attacks, but showed some limitations in ransomware defense.


- Incorporating network flow data to capture additional threat patterns.
- Expanding the attack prevention model to handle other attack types beyond DDoS and ransomware.
- Testing and deploying the model in real-world IoT environments.


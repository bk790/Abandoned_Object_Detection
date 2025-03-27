# Abandoned Object Detection

## Overview
Abandoned Object Detection is a computer vision-based system that identifies unattended objects in public spaces using deep learning and image processing techniques. This project is designed to enhance security measures by detecting objects left behind and triggering alerts for further investigation.

## Features
- **Real-time Object Detection**: Uses pre-trained deep learning models to detect objects in video frames.
- **Background Subtraction**: Differentiates static objects from moving ones to identify abandoned items.
- **Time-Based Tracking**: Monitors objects left unattended for a predefined duration.
- **Alert Mechanism**: Triggers notifications or alarms upon detecting abandoned objects.
- **Customizable Sensitivity**: Adjustable detection parameters for various environments.

## Technologies Used
- **Programming Language**: Python
- **Frameworks & Libraries**: OpenCV, TensorFlow/PyTorch, NumPy, DeepFace (for panic detection)
- **Model**: Pre-trained CNN-based object detection (YOLO, Faster R-CNN, or SSD)
- **Deployment**: Flask/Django (optional for API integration)

## Installation
### Prerequisites
Ensure you have Python installed on your system.

```sh
pip install opencv-python numpy tensorflow torch torchvision deepface flask
```

### Clone Repository
```sh
git clone https://github.com/your-repo/abandoned-object-detection.git
cd abandoned-object-detection
```

## Usage
1. Run the detection script:
   ```sh
   python detect_abandoned_objects.py
   ```
2. Adjust parameters in `config.py` for different environments.
3. The system will process video feeds and highlight abandoned objects.

## Configuration
Modify `config.py` to fine-tune detection parameters such as:
- **Detection Threshold**
- **Time to Trigger Alarm**
- **Frame Sampling Rate**

## Output
![Detection Output](output.png)

## Demo
Include images, GIFs, or a link to a demo video showcasing the detection in action.

## Future Enhancements
- Integration with security camera systems
- Cloud-based alert system with remote monitoring
- Multi-object tracking for crowded environments

## Contributors
- Your Name ([GitHub Profile](https://github.com/your-profile))

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


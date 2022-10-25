# BL-JUNIPER-A-CNN-Assisted-Framework-for-Perceptual-Video-Coding-Leveraging-Block-Level-JND

### Introduction

This is the implementation of [BL-JUNIPER: A CNN-Assisted Framework for Perceptual Video Coding Leveraging Block-Level JND](https://ieeexplore.ieee.org/abstract/document/9810507) paper in Keras and Matlab

**Abstract**

Just Noticeable Distortion (JND) finds the minimum distortion level perceivable by humans. This can be a natural solution for setting the compression for each video region in perceptual video coding. However, existing JND-based solutions estimate JND levels for each video frame and ignore the fact that different video regions have different perceptual importance. To address this issue, we propose a Block-Level Just Noticeable Distortion-based Perceptual (BL-JUNIPER) framework for video coding. The proposed four-stage framework combines different perceptual information to further improve the prediction accuracy. The JND mapping in the first stage derives block-level JNDs from frame-level information without the need to collect a new bock-level JND dataset. In the second stage, an efficient CNNbased model is proposed to predict JND levels for each block according to spatial and temporal characteristics. Unlike existing methods, BL-JUNIPER works on raw video frames and avoids reencoding each frame several times, making it computationally practical. Third, the visual importance of each block is measured using a visual attention model. Finally, a proposed quantization control algorithm uses both JND levels and visual importance to adjust the Quantization Parameter (QP) for each block. The specific algorithm for each stage of the proposed framework can be changed, as long as the input and output formats of each block are followed, without the need to change other stages, based on any current or future methods, providing a flexible and robust solution. Extensive experimental results demonstrate that BLJUNIPER achieves a mean bitrate reduction of 27.75% with a Delta Mean Opinion Score (DMOS) close to zero and BD-Rate gains of 25.44% based on MOS, compared to the baseline encoding, and also gains a better performance compared to competing methods.

**The proposed BL-JUNIPER framework:**

![image](https://user-images.githubusercontent.com/59918141/197768571-20a1aa16-30f0-45ac-ad0b-e798f534950f.png)


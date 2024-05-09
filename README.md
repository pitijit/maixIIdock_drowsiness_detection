# maix-II-dock drowsiness detection
Project of ICT740 Hardware Designs for Artificial Intelligence and Internet of Things (TAIST-Tokyo Tech).<br />
### Team Members:<br />
6622040266 Pitijit Charoenwuttikajorn (SIIT)<br />
6622040670 Onsasipat Kasamrach (SIIT)<br />
6622040316 Pongpon Lapsatid (SIIT)

![Screenshot (987)](https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/36162acf-c6ca-4c1e-85e2-00a3073f0090)

eyes detection (opened/closed) with maix II dock board (M2dock).<br />
### Overview<br />
![Overview_3Frames](https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/52a969bb-512f-44aa-9d76-458f12fb8bcd)<br />
### Flowchart<br />
![FlowChart_3Frame](https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/df305e02-5f9f-4675-9579-b0a931b85120)<br />

### Model Training<br />
1. Develop model for object detection with MaixHub.<br />
   1.1. Gather and organize the dataset for the object detection task.<br />
   ![Screenshot (992) - Copy](https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/9b2662a3-bf30-4d83-85f1-5df9b0b1b255)
   1.2. Annotate the dataset with bounding boxes for each image in the dataset as either “opened” or “closed” eyes. Common annotation formats include the YOLO format.<br />
   ![Screenshot (992)](https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/e5446f4b-1f13-46bc-9e58-c42aba3a0cd2)

2. Training dataset with information below.<br />
  ![Screenshot (991)](https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/64443f9f-9ad7-4b4c-9b03-dd0a6788e2ec)
   
3. The evaluation of this model.<br />
  ![Screenshot (980)](https://github.com/pitijit/maix_II_eyes_detection/assets/85090124/b4528add-a79e-4f42-88a0-d6899bf2ee9c)
  
4. Deploy to  maix II dock board.<br />
  ![Screenshot (998)](https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/6d5445e0-e767-4689-b568-8bfeefaa0a5c)

5. Open interactive shell with adb driver.(I used web adb https://app.webadb.com/)<br />
7. Add folder of drowsiness_detection (all files in my repo) to root.<br />
8. Run file main.py.<br />
9. Results.<br />
   ![S__67854345_0](https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/9c82e187-7109-4f99-a088-68259ec116d4) 
   ![S__67854347_0](https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/8795d27d-a0da-4b5c-b94b-5f0859f289fa)
   ![S__67854348_0](https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/c670349a-1fa8-42a5-bc07-58213a9b83c4)<br />
Video:<br />
https://github.com/pitijit/maixIIdock_drowsiness_detection/assets/85090124/4543fd23-7e79-4bf9-a1d3-8bdfd0b194b1<br />
https://youtube.com/shorts/LvFnWsxRuRs?feature=share


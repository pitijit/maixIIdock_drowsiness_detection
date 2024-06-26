# generated by maixhub, tested on maixpy3 v0.4.8
from maix import nn, camera, display, image
import serial

input_size = (224, 224)
model = "model-121973.awnn.mud"
labels = ['opened', 'closed']
anchors = [2.44, 0.94, 2.55, 1.16, 2.91, 1.09, 3.09, 1.22, 3.59, 1.44]

class Comm:
    def __init__(self, uart):
        self.uart = uart

    def send_detect_result(self, boxes, probs, labels):
        msg = ""
        for i, box in enumerate(boxes):
            idx = probs[i][0]
            p = probs[i][1][idx]
            label = labels[idx]
            msg += "{}:{}:{}:{}:{}:{:.2f}:{}, ".format(box[0], box[1], box[2], box[3], idx, p, label)
        if msg:
            msg = msg[:-2] + "\n"
        self.uart.write(msg.encode())

def init_uart():
    uart = serial.Serial("/dev/ttyS1",115200)
    return uart

class YOLOv2:
    def __init__(self, model_path, labels, anchors, net_in_size, net_out_size):
        self.labels = labels
        self.anchors = anchors
        self.net_in_size = net_in_size
        self.net_out_size = net_out_size
        print("-- load model:", model)
        self.model = nn.load(model_path)
        print("-- load ok")
        print("-- init yolo2 decoder")
        self._decoder = nn.decoder.Yolo2(len(labels), anchors, net_in_size=net_in_size, net_out_size=net_out_size)
        print("-- init complete")

    def run(self, img, nms=0.3, threshold=0.5):
        out = self.model.forward(img, layout="hwc")
        boxes, probs = self._decoder.run(out, nms=nms, threshold=threshold, img_size=input_size)
        return boxes, probs

    def draw(self, img, boxes, probs):
        for i, box in enumerate(boxes):
            class_id = probs[i][0]
            prob = probs[i][1][class_id]
            msg = "{}:{:.2f}%".format(self.labels[class_id], prob*100)
            img.draw_rectangle(box[0], box[1], box[0] + box[2], box[1] + box[3], color=(255, 255, 255), thickness=2)
            img.draw_string(box[0] + 2, box[1] + 2, msg, scale = 1.2, color = (255, 255, 255), thickness = 2)

# Alert message
alert_message = "Alert Message"

def main():
    camera.config(size=input_size)
    yolov2 = YOLOv2(model, labels, anchors, input_size, (input_size[0] // 32, input_size[1] // 32))
    uart = init_uart()
    comm = Comm(uart)
    closed_count = 0  # Initialize the count of "closed" labels
    last_detection_time = time.time()  # Initialize the time of the last detection
    while True:
        img = camera.capture()
        boxes, probs = yolov2.run(img, nms=0.3, threshold=0.5)
        yolov2.draw(img, boxes, probs)
        comm.send_detect_result(boxes, probs, labels)

        # Check if the "closed" label is detected continuously
        closed_detected = any(labels[prob[0]] == 'closed' for prob in probs)
        if closed_detected:
            closed_count += 1
        else:
            closed_count = 0

        # Check if the "closed" label is detected three or more times continuously
        if closed_count >= 3:
            current_time = time.time()
            if current_time - last_detection_time >= 3:  # Check if 3 seconds have elapsed since the last detection
                # Draw the alert message on the image
                img.draw_string(20, 10, "{}".format(alert_message), color=(255, 0, 0), scale=1.5, thickness=2)
                display.show(img)  # Display the image with the alert message
                last_detection_time = current_time  # Update the last detection time
            else:
                display.show(img)  # Show the original image if the condition is not met
        else:
            display.show(img)  # Show the original image if the condition is not met

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback, time
        msg = traceback.format_exc()
        print(msg)
        img = image.new(size = (240, 240), color = (255, 0, 0), mode = "RGB")
        img.draw_string(0, 0, msg, scale = 0.8, color = (0, 0, 255), thickness = 1)
        display.show(img)
        time.sleep(30)

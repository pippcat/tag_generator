def generate_frames():
    while True:
        # Read frame from the camera
        success, frame = camera.read()
        if not success:
            break

        # Convert the frame to grayscale for barcode detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect barcodes in the frame
        retval, decoded_info, points, straight_qrcode = barcode_detector.detectAndDecodeMulti(gray_frame)

        # Display the frame with barcode information
        frame_with_overlay = frame.copy()

        if retval:
            for info in decoded_info:
                cv2.putText(frame_with_overlay, f"Barcode: {info}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        ret, buffer = cv2.imencode('.jpg', frame_with_overlay)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

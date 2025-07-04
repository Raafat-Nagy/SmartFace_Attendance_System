import cv2
from src import FaceRecognition, CSVLogger
from src.api.send_attendance_api import send_attendance


def run_recognition(
    encodings_file: str,
    hall_id: int = 1,
    send_api: bool = True,
    log_csv: bool = True,
    csv_path: str = "attendance_records/attendance.csv",
):
    """
    Runs the real-time face recognition system with optional attendance logging and API integration.

    Args:
        encodings_file (str): Path to the .pkl file containing known face encodings.
        hall_id (int): ID of the lecture hall used when sending attendance (default is 1).
        send_api (bool): If True, send attendance to the remote API (default is True).
        log_csv (bool): If True, save attendance locally to a CSV file (default is True).
        csv_path (str): Path to the CSV file used for logging attendance.
    """
    recognizer = FaceRecognition(encodings_file)
    logger = CSVLogger(csv_path) if log_csv else None
    logged_students = set()

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        face_names, _ = recognizer.detect_known_faces(frame)

        for name in face_names:
            if name != "Unknown" and name not in logged_students:
                if send_api:
                    send_attendance(hall_id=hall_id, student_tag=name)
                if logger:
                    logger.log_attendance(name)
                print(f"Detected: {name}")
                logged_students.add(name)

        cv2.imshow("Live Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    encodings_file = "models/encodings.pkl"
    hall_id = 1
    send_api = True
    log_csv = True
    csv_path = "attendance_records/attendance.csv"

    run_recognition(
        encodings_file=encodings_file,
        hall_id=hall_id,
        send_api=send_api,
        log_csv=log_csv,
        csv_path=csv_path,
    )

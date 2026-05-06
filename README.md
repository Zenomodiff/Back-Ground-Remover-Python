# 🖼️ Batch-BG-Remover-Py

An automated CLI tool designed to batch-process image background removal using the **remove.bg** REST API. This script is built to streamline workflows for creators, engineers, and hobbyists who need transparent assets for 3D printing (lithophanes), DIY electronics documentation, or YouTube thumbnails.

---

## 🚀 Features
*   **Batch Processing:** Scans an entire directory and processes all images in one command.
*   **Smart Filtering:** Automatically identifies and processes `.jpg`, `.jpeg`, and `.png` files while ignoring system junk.
*   **Automated I/O:** Creates organized input/output folders automatically.
*   **Error Handling:** Manages API rate limits and provides clear feedback on credit status.

---

## 🛠️ Technical Stack
*   **Language:** Python 3.x
*   **Libraries:** 
    *   `Requests`: Handles binary data streaming via HTTP.
    *   `OS`: Manages local filesystem mapping and pathing.
*   **Logic:** Implements a filtered iterator loop to handle multiple files without manual intervention.

---

## 💻 Setup & Usage

### 1. Prerequisites
Ensure you have Python installed and install the required dependency:
```bash
pip install requests

# Apple Device Info (NVDA Add-on)

Apple Device Info is an NVDA add-on that announces basic information about Apple devices connected to Windows using the Apple Devices Windows application.

It allows blind and low-vision users to quickly check whether an iPhone or iPad is detected and hear available storage details.

---

## Features

- Detects connected Apple devices
- Announces device model name
- Announces total storage capacity
- Announces available storage space
- Supports multiple connected devices (announces count and first device)
- Manual refresh of device information

---

## Keyboard Shortcuts

- NVDA+Alt+D : Announce Apple device summary  
- NVDA+Alt+S : Announce storage information  
- NVDA+Alt+R : Refresh device information  

---

## Example Announcements

- Apple device. Model iPhone 15 Pro. Storage capacity 256 GB. Available space 192 GB.  
- 2 Apple devices detected. First device. Model iPhone 14. Storage capacity 128 GB. Available space 40 GB.

---

## Requirements

- Windows with Apple Devices (Apple’s official Windows application) installed  
- NVDA 2024.1 or later  

---

## Known Limitations

- Battery level is not available due to Windows and Apple platform limitations  
- Only information exposed through the Apple Devices Windows interface can be detected  
- Advanced device management features are not supported  

---

## Installation

1. Download the AppleDeviceInfo NVDA add-on package  
2. Open the file with NVDA  
3. Restart NVDA when prompted  

---

## Author

Rajath Tirumangalam

---

## License

GNU General Public License version 2 (GPL v2)

---

## Changelog

### Version 1.0
- Initial public release  
- Device detection  
- Storage and available space announcements  
- Refresh command  

# Apple Devices NVDA AppModule - V2.1
# Author: Rajath Tirumangalam
#
# NVDA+Alt+D -> Device summary (first device)
# NVDA+Alt+S -> Storage info (first device)
# NVDA+Alt+R -> Refresh device information

import appModuleHandler
import scriptHandler
import ui
import api

MAX_NODES = 250


class AppModule(appModuleHandler.AppModule):

    _cachedLines = []

    # ------------------------------------------------------
    # Utility
    # ------------------------------------------------------

    def _getRoot(self):
        return api.getForegroundObject()

    # ------------------------------------------------------
    # Scan for ALL device info lines
    # ------------------------------------------------------

    def _scanForDeviceLines(self):
        root = self._getRoot()
        if not root:
            return []

        queue = [root]
        scanned = 0
        found = []

        while queue and scanned < MAX_NODES:
            obj = queue.pop(0)
            scanned += 1

            try:
                name = obj.name
                if (
                    name
                    and "iPhone" in name
                    and "GB" in name
                    and "·" in name
                    and "(" in name
                ):
                    if name not in found:
                        found.append(name)
            except:
                pass

            try:
                for child in obj.children:
                    queue.append(child)
            except:
                pass

        return found

    # ------------------------------------------------------
    # Cached getter
    # ------------------------------------------------------

    def _getDeviceLines(self):
        if self._cachedLines:
            return self._cachedLines

        lines = self._scanForDeviceLines()
        self._cachedLines = lines
        return lines

    def _clearCache(self):
        self._cachedLines = []

    # ------------------------------------------------------
    # Parse:
    # iPhone 17 Pro · 256 GB (192 GB Available)
    # ------------------------------------------------------

    def _parseDeviceLine(self, line):
        model = None
        total = None
        available = None

        try:
            left, right = line.split("·", 1)
            model = left.strip()

            storage = right.strip()
            total = storage.split("(")[0].strip()

            inside = storage.split("(")[1]
            available = (
                inside.replace(")", "")
                .replace("Available", "")
                .strip()
            )
        except:
            pass

        return model, total, available

    # ------------------------------------------------------
    # Scripts
    # ------------------------------------------------------

    @scriptHandler.script(
        description="Announce Apple device summary",
        gesture="kb:NVDA+alt+d"
    )
    def script_deviceSummary(self, gesture):

        lines = self._getDeviceLines()

        if not lines:
            ui.message("No Apple device detected")
            return

        count = len(lines)

        first = lines[0]
        model, total, available = self._parseDeviceLine(first)

        speech = ""

        if count == 1:
            speech += "Apple device. "
        else:
            speech += f"{count} Apple devices detected. First device. "

        if model:
            speech += f"Model {model}. "
        if total:
            speech += f"Storage capacity {total}. "
        if available:
            speech += f"Available space {available}."

        ui.message(speech)

    @scriptHandler.script(
        description="Announce Apple device storage",
        gesture="kb:NVDA+alt+s"
    )
    def script_deviceStorage(self, gesture):

        lines = self._getDeviceLines()

        if not lines:
            ui.message("Storage information not found")
            return

        first = lines[0]
        model, total, available = self._parseDeviceLine(first)

        speech = ""

        if model:
            speech += f"{model}. "
        if total:
            speech += f"Total storage {total}. "
        if available:
            speech += f"Available {available}."

        ui.message(speech)

    @scriptHandler.script(
        description="Refresh Apple device information",
        gesture="kb:NVDA+alt+r"
    )
    def script_refresh(self, gesture):

        self._clearCache()
        lines = self._getDeviceLines()

        if not lines:
            ui.message("Refreshed. No Apple device detected")
        else:
            ui.message(f"Refreshed. {len(lines)} Apple device(s) found.")

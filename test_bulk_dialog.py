"""
Test r�pido para verificar BulkItemDialog
"""

import sys
from PyQt6.QtWidgets import QApplication
from src.views.dialogs.bulk_item_dialog import BulkItemDialog

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Crear y mostrar el di�logo
    dialog = BulkItemDialog("Test Category")

    if dialog.exec():
        # Si se acept�, mostrar los items
        items = dialog.get_items_data()
        print(f"\n Se crearon {len(items)} items:")
        for i, item in enumerate(items):
            print(f"  {i+1}. Label: '{item['label']}' | Tags: {item['tags']}")
    else:
        print("\nL Di�logo cancelado")

    sys.exit(0)
